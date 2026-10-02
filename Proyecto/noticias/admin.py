from django.contrib import admin
from .models import Categoria, Noticia


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'total_noticias')
    search_fields = ('nombre',)
    ordering = ('nombre',)

    def total_noticias(self, obj):
        return obj.noticias.count()
    total_noticias.short_description = "N° de noticias"


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha', 'destacado')
    list_filter = ('categoria', 'destacado', 'fecha')
    search_fields = ('titulo', 'resumen', 'contenido')
    autocomplete_fields = ('categoria',)
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
