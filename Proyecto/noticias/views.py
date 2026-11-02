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

def buscar(request):
    termino = request.GET.get('q', '')
    resultados = Noticia.objects.filter(titulo__icontains=termino) if termino else Noticia.objects.none()
    contexto = {
        'noticias': resultados,
        'termino': termino,
    }
    return render(request, 'noticias/inicio.html', contexto)
