import json
from django.conf import settings
from django.core.management.base import BaseCommand
from noticias.models import Categoria, Noticia


class Command(BaseCommand):
    help = "Migra la información de data/noticias.json hacia la base de datos relacional."

    def handle(self, *args, **options):
        ruta_json = settings.BASE_DIR / 'data' / 'noticias.json'
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            noticias = json.load(archivo)

        creadas, actualizadas = 0, 0
        for item in noticias:
            categoria, _ = Categoria.objects.get_or_create(nombre=item['categoria'])
            noticia, fue_creada = Noticia.objects.update_or_create(
                titulo=item['titulo'],
                defaults={
                    'categoria': categoria,
                    'fecha': item['fecha'],
                    'resumen': item['resumen'],
                    'contenido': item['contenido'],
                    'destacado': item.get('destacado', False),
                    'imagen': item['imagen'],
                }
            )
            creadas += 1 if fue_creada else 0
            actualizadas += 0 if fue_creada else 1

        self.stdout.write(self.style.SUCCESS(
            f"Noticias migradas: {creadas} creadas, {actualizadas} actualizadas."
        ))
