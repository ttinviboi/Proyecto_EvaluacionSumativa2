from django.db import models
from django.contrib.auth.models import User
from cine.models import Pelicula


class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reservas')
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT, related_name='reservas')
    fecha = models.DateField(verbose_name='Fecha de función')
    cantidad = models.PositiveSmallIntegerField(default=1, verbose_name='Entradas')
    estado = models.CharField(max_length=12, choices=ESTADOS, default='pendiente')
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creada']
        constraints = [models.UniqueConstraint(fields=['usuario', 'pelicula', 'fecha'], name='reserva_unica_por_usuario_funcion')]
        permissions = [('gestionar_reservas', 'Puede gestionar todas las reservas')]

    def __str__(self):
        return f'{self.pelicula} - {self.usuario} ({self.fecha})'
