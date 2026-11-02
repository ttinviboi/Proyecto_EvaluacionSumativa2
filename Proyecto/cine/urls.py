from django.urls import path
from . import views

app_name = 'cine'

urlpatterns = [
    path('', views.cartelera, name='cartelera'),
    path('buscar/', views.buscar, name='buscar'),
    path('<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
]
