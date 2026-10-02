from django.contrib import admin
from .models import Genero, Pelicula


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'total_peliculas')
    search_fields = ('nombre',)
    ordering = ('nombre',)

    def total_peliculas(self, obj):
        return obj.peliculas.count()
    total_peliculas.short_description = "N° de películas"


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'genero', 'anio', 'calificacion', 'estreno')
    list_filter = ('genero', 'estreno', 'anio')
    search_fields = ('titulo', 'director', 'sinopsis')
    autocomplete_fields = ('genero',)
    ordering = ('-anio',)
