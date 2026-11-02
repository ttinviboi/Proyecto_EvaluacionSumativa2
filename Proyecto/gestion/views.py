from functools import wraps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from cine.models import Genero, Pelicula
from noticias.models import Categoria, Noticia
from .forms import CategoriaForm, CrearUsuarioForm, GeneroForm, ReservaForm
from .models import Reserva

ROLE_ADMIN = 'Administrador'
ROLE_SUPERVISOR = 'Supervisor'
ROLE_STAFF = 'Administrativo'


def role_of(user):
    if user.is_superuser or user.groups.filter(name=ROLE_ADMIN).exists(): return ROLE_ADMIN
    for role in (ROLE_SUPERVISOR, ROLE_STAFF):
        if user.groups.filter(name=role).exists(): return role
    return None


def roles_required(*roles):
    def decorator(view):
        @login_required
        @wraps(view)
        def wrapped(request, *args, **kwargs):
            if role_of(request.user) not in roles: raise PermissionDenied
            return view(request, *args, **kwargs)
        return wrapped
    return decorator


class PortalLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    def get_success_url(self): return reverse_lazy('gestion:dashboard')


@login_required
def dashboard(request):
    perfil = role_of(request.user)
    if not perfil: raise PermissionDenied('Solicita al administrador que te asigne un perfil.')
    reservas_count = Reserva.objects.count() if perfil in (ROLE_ADMIN, ROLE_SUPERVISOR) else Reserva.objects.filter(usuario=request.user).count()
    return render(request, 'gestion/dashboard.html', {
        'perfil': perfil,
        'noticias_count': Noticia.objects.count() if perfil != ROLE_STAFF else None,
        'peliculas_count': Pelicula.objects.count(),
        'reservas_count': reservas_count,
        'usuarios_count': User.objects.count() if perfil == ROLE_ADMIN else None,
    })


def _mantenedor(request, model, titulo, nombre):
    q = request.GET.get('q', '').strip()
    objects = model.objects.filter(nombre__icontains=q) if q else model.objects.all()
    return render(request, 'gestion/mantenedor_lista.html', {
        'objetos': objects, 'titulo': titulo, 'nombre': nombre, 'q': q,
        'can_delete': role_of(request.user) == ROLE_ADMIN,
        'can_manage': role_of(request.user) in (ROLE_ADMIN, ROLE_SUPERVISOR),
        'create_url': f'gestion:{nombre}_crear', 'edit_url': f'gestion:{nombre}_editar',
        'delete_url': f'gestion:{nombre}_eliminar',
    })


def _mantenedor_form(request, model, form_class, titulo, nombre, object_id=None):
    obj = get_object_or_404(model, pk=object_id) if object_id else None
    form = form_class(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save(); messages.success(request, f'{titulo} guardado correctamente.')
        return redirect(f'gestion:{nombre}_lista')
    return render(request, 'gestion/formulario.html', {'form': form, 'titulo': titulo, 'volver': f'gestion:{nombre}_lista'})


@roles_required(ROLE_ADMIN, ROLE_SUPERVISOR)
def categorias(request): return _mantenedor(request, Categoria, 'Categorías de noticias', 'categorias')
@roles_required(ROLE_ADMIN, ROLE_SUPERVISOR)
def categoria_crear(request): return _mantenedor_form(request, Categoria, CategoriaForm, 'Categoría', 'categorias')
@roles_required(ROLE_ADMIN, ROLE_SUPERVISOR)
def categoria_editar(request, pk): return _mantenedor_form(request, Categoria, CategoriaForm, 'Categoría', 'categorias', pk)
@roles_required(ROLE_ADMIN)
@require_POST
def categoria_eliminar(request, pk):
    get_object_or_404(Categoria, pk=pk).delete(); messages.success(request, 'Categoría eliminada.'); return redirect('gestion:categorias_lista')

@roles_required(ROLE_ADMIN, ROLE_SUPERVISOR)
def generos(request): return _mantenedor(request, Genero, 'Géneros de cine', 'generos')
@roles_required(ROLE_ADMIN, ROLE_SUPERVISOR)
def genero_crear(request): return _mantenedor_form(request, Genero, GeneroForm, 'Género', 'generos')
@roles_required(ROLE_ADMIN, ROLE_SUPERVISOR)
def genero_editar(request, pk): return _mantenedor_form(request, Genero, GeneroForm, 'Género', 'generos', pk)
@roles_required(ROLE_ADMIN)
@require_POST
def genero_eliminar(request, pk):
    get_object_or_404(Genero, pk=pk).delete(); messages.success(request, 'Género eliminado.'); return redirect('gestion:generos_lista')

@roles_required(ROLE_ADMIN)
def usuarios(request):
    form = CrearUsuarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(); messages.success(request, 'Usuario creado y perfil asignado.'); return redirect('gestion:usuarios')
    return render(request, 'gestion/usuarios.html', {'form': form, 'usuarios': User.objects.prefetch_related('groups').order_by('username')})

@login_required
def crear_reserva(request):
    if not role_of(request.user): raise PermissionDenied
    form = ReservaForm(request.POST or None, initial={'usuario': request.user})
    if request.method == 'POST' and form.is_valid():
        reserva = form.save(commit=False); reserva.usuario = request.user; reserva.save()
        messages.success(request, 'Reserva registrada correctamente.'); return redirect('gestion:reservas')
    return render(request, 'gestion/formulario.html', {'form': form, 'titulo': 'Nueva reserva de cine', 'volver': 'gestion:reservas'})

@login_required
def reservas(request):
    perfil = role_of(request.user)
    if not perfil: raise PermissionDenied
    qs = Reserva.objects.select_related('usuario', 'pelicula__genero')
    if perfil not in (ROLE_ADMIN, ROLE_SUPERVISOR): qs = qs.filter(usuario=request.user)
    return render(request, 'gestion/reservas.html', {'reservas': qs, 'perfil': perfil, 'estados': Reserva.ESTADOS})

@roles_required(ROLE_ADMIN, ROLE_SUPERVISOR)
@require_POST
def cambiar_estado_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    estado = request.POST.get('estado')
    if estado not in dict(Reserva.ESTADOS): raise PermissionDenied
    reserva.estado = estado; reserva.save(update_fields=['estado']); messages.success(request, 'Estado de reserva actualizado.')
    return redirect('gestion:reservas')
