from django.db import models


class Categoria(models.Model):
    """Categoría temática a la que pertenece una noticia (ej: Desarrollo Web, IA)."""
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    """Noticia publicada en el portal, relacionada a una Categoría."""
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='noticias',
        verbose_name="Categoría"
    )
    fecha = models.DateField()
    resumen = models.TextField()
    contenido = models.TextField()
    destacado = models.BooleanField(default=False)
    imagen = models.CharField(
        max_length=255,
        help_text="Ruta relativa dentro de static/img/, ej: noticias/django.jfif"
    )

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo
