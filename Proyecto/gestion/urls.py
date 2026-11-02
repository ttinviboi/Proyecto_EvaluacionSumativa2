from django.urls import path
from . import views

app_name = 'gestion'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categorias/', views.categorias, name='categorias_lista'),
    path('categorias/nueva/', views.categoria_crear, name='categorias_crear'),
    path('categorias/<int:pk>/editar/', views.categoria_editar, name='categorias_editar'),
    path('categorias/<int:pk>/eliminar/', views.categoria_eliminar, name='categorias_eliminar'),
    path('generos/', views.generos, name='generos_lista'),
    path('generos/nuevo/', views.genero_crear, name='generos_crear'),
    path('generos/<int:pk>/editar/', views.genero_editar, name='generos_editar'),
    path('generos/<int:pk>/eliminar/', views.genero_eliminar, name='generos_eliminar'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('reservas/', views.reservas, name='reservas'),
    path('reservas/nueva/', views.crear_reserva, name='reserva_crear'),
    path('reservas/<int:pk>/estado/', views.cambiar_estado_reserva, name='reserva_estado'),
]
