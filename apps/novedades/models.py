from django.db import models
from apps.domiciliarios.models import Domiciliarios 
from apps.solicitud.models import Solicitud 

class Novedades(models.Model):
    domiciliarios = models.ForeignKey(Domiciliarios, on_delete=models.SET_NULL , null=True,  blank=True)
    solicitud = models.ForeignKey(Solicitud,  on_delete=models.SET_NULL, null=True,  blank=True)
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
