from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar/', views.buscar, name='buscar'),
    path('agregar/', views.agregar, name='agregar'),
    path('<int:noticia_id>/', views.detalle, name='detalle'),
    path('<int:noticia_id>/modificar/', views.modificar, name='modificar'),
    path('<int:noticia_id>/eliminar/', views.eliminar, name='eliminar'),
]
