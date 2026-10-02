from django.shortcuts import render, get_object_or_404
from .models import Noticia


def inicio(request):
    """Listado de noticias obtenido mediante Django ORM."""
    noticias = Noticia.objects.select_related('categoria').all()
    contexto = {
        'noticias': noticias
    }
    return render(request, 'noticias/inicio.html', contexto)


def detalle(request, noticia_id):
    """Detalle de una noticia puntual, obtenido mediante Django ORM."""
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    contexto = {
        'noticia': noticia
    }
    return render(request, 'noticias/detalle.html', contexto)


# --- Vistas placeholder de operaciones CRUD ---
# Se implementarán de forma funcional en la siguiente evaluación sumativa.
# Por ahora exponen la ruta y una interfaz visual, tal como exige la pauta.

def agregar(request):
    return render(request, 'noticias/en_construccion.html', {'accion': 'Agregar noticia'})


def modificar(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticias/en_construccion.html', {
        'accion': f'Modificar noticia: {noticia.titulo}'
    })


def eliminar(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticias/en_construccion.html', {
        'accion': f'Eliminar noticia: {noticia.titulo}'
    })


def buscar(request):
    termino = request.GET.get('q', '')
    resultados = Noticia.objects.filter(titulo__icontains=termino) if termino else Noticia.objects.none()
    contexto = {
        'noticias': resultados,
        'termino': termino,
    }
    return render(request, 'noticias/inicio.html', contexto)
