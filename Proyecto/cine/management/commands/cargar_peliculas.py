import json
from django.conf import settings
from django.core.management.base import BaseCommand
from cine.models import Genero, Pelicula


class Command(BaseCommand):
    help = "Migra la información de data/peliculas.json hacia la base de datos relacional."

    def handle(self, *args, **options):
        ruta_json = settings.BASE_DIR / 'data' / 'peliculas.json'
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            peliculas = json.load(archivo)

        creadas, actualizadas = 0, 0
        for item in peliculas:
            genero, _ = Genero.objects.get_or_create(nombre=item['genero'])
            pelicula, fue_creada = Pelicula.objects.update_or_create(
                titulo=item['titulo'],
                defaults={
                    'director': item['director'],
                    'genero': genero,
                    'anio': item['anio'],
                    'calificacion': item['calificacion'],
                    'sinopsis': item['sinopsis'],
                    'estreno': item.get('estreno', False),
                    'imagen': item['imagen'],
                }
            )
            creadas += 1 if fue_creada else 0
            actualizadas += 0 if fue_creada else 1

        self.stdout.write(self.style.SUCCESS(
            f"Películas migradas: {creadas} creadas, {actualizadas} actualizadas."
        ))
