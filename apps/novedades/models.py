from django.db import models
from apps.domiciliarios.models import Domiciliarios 
from apps.solicitud.models import Solicitud 

class Novedades(models.Model):
    domiciliarios = models.ForeignKey(Domiciliarios, null=True, on_delete=models.SET_NULL)
    solicitud = models.ForeignKey(Solicitud, null=True, on_delete=models.SET_NULL)
    descripcion = models.TextField()
    
    class EstadoChoices(models.TextChoices):
        ABIERTO = 'abierto', 'Abierto'
        CERRADO = 'cerrado', 'Cerrado'
    
    estado = models.CharField(
        max_length=15,
        choices=EstadoChoices.choices,
        default=EstadoChoices.ABIERTO,
    )
    
    fecha_reporte = models.DateTimeField()
    
    def __str__(self):
        return f"Novedad {self.id} - {self.estado}"
