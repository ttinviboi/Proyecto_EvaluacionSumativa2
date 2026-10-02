from django.urls import path
from . import views

app_name = 'cine'

urlpatterns = [
    path('', views.cartelera, name='cartelera'),
    path('buscar/', views.buscar, name='buscar'),
    path('agregar/', views.agregar, name='agregar'),
    path('<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('<int:pelicula_id>/modificar/', views.modificar, name='modificar'),
    path('<int:pelicula_id>/eliminar/', views.eliminar, name='eliminar'),
]
