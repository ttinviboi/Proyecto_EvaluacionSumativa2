from django.shortcuts import render, get_object_or_404
from .models import Pelicula


def cartelera(request):
    """Listado de películas obtenido mediante Django ORM."""
    peliculas = Pelicula.objects.select_related('genero').all()
    contexto = {
        'peliculas': peliculas
    }
    return render(request, 'cine/cartelera.html', contexto)


def detalle_pelicula(request, pelicula_id):
    """Detalle de una película puntual, obtenido mediante Django ORM."""
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    contexto = {
        'pelicula': pelicula
    }
    return render(request, 'cine/detalle_pelicula.html', contexto)


# --- Vistas placeholder de operaciones CRUD ---
# Se implementarán de forma funcional en la siguiente evaluación sumativa.

def agregar(request):
    return render(request, 'cine/en_construccion.html', {'accion': 'Agregar película'})


def modificar(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    return render(request, 'cine/en_construccion.html', {
        'accion': f'Modificar película: {pelicula.titulo}'
    })


def eliminar(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    return render(request, 'cine/en_construccion.html', {
        'accion': f'Eliminar película: {pelicula.titulo}'
    })


def buscar(request):
    termino = request.GET.get('q', '')
    resultados = Pelicula.objects.filter(titulo__icontains=termino) if termino else Pelicula.objects.none()
    contexto = {
        'peliculas': resultados,
        'termino': termino,
    }
    return render(request, 'cine/cartelera.html', contexto)
