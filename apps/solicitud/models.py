from django.db import models
from apps.usuarios.models import Usuarios
from apps.domiciliarios.models import Domiciliarios  

class Solicitud(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'PENDIENTE'
        ASIGNADO = 'ASIGNADO', 'ASIGNADO'
        EN_CURSO = 'EN CURSO', 'EN CURSO'
        COMPLETADO = 'COMPLETADO', 'COMPLETADO'
        REPROGRAMADO = 'REPROGRAMADO', 'REPROGRAMADO'
        CANCELADO = 'CANCELADO', 'CANCELADO'
    
    usuarios = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, blank=True)
    domiciliarios = models.ForeignKey(Domiciliarios, on_delete=models.SET_NULL, null=True, blank=True)
    direccion_recogida = models.CharField(max_length=200)
    direccion_entrega = models.CharField(max_length=200)
    estado = models.CharField(
        max_length=12,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    fecha_hora = models.DateTimeField()
    
    def __str__(self):
        return f"Solicitud {self.id} - {self.get_estado_display()}"
