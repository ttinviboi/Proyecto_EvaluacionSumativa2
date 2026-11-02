from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar/', views.buscar, name='buscar'),
    path('<int:noticia_id>/', views.detalle, name='detalle'),
]
