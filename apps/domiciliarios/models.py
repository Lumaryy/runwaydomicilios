from django.db import models
from apps.usuarios.models import Usuarios  

class Domiciliarios(models.Model):
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.SET_NULL)
    licencia_vehiculo = models.CharField(max_length=50)
    
    class DisponibilidadChoices(models.TextChoices):
        DISPONIBLE = 'disponible', 'Disponible'
        OCUPADO = 'ocupado', 'Ocupado'
        NO_DISPONIBLE = 'no_disponible', 'No Disponible'
    
    disponibilidad = models.CharField(
        max_length=15,
        choices=DisponibilidadChoices.choices,
        default=DisponibilidadChoices.DISPONIBLE,
    )
    
    def __str__(self):
        return f"Domiciliario {self.usuarios.nombre if self.usuarios else 'Sin usuario'}"
