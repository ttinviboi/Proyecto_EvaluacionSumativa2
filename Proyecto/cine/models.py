from django.db import models


class Genero(models.Model):
    """Género cinematográfico (ej: Ciencia Ficción, Drama, Terror)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    """Película de la cartelera, relacionada a un Género."""
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=150)
    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        related_name='peliculas',
        verbose_name="Género"
    )
    anio = models.PositiveIntegerField(verbose_name="Año")
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    sinopsis = models.TextField()
    estreno = models.BooleanField(default=False)
    imagen = models.CharField(
        max_length=255,
        help_text="Ruta relativa dentro de static/img/, ej: cine/inception.jpg"
    )

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ['-anio']

    def __str__(self):
        return self.titulo
