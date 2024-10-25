from django.db import models
from apps.usuarios.models import Usuarios
from apps.domiciliarios.models import Domiciliarios  

class Solicitud(models.Model):
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.SET_NULL)
    domiciliarios = models.ForeignKey(Domiciliarios, null=True, on_delete=models.SET_NULL)
    direccion_recogida = models.CharField(max_length=200)
    direccion_entrega = models.CharField(max_length=200)
    estado = models.CharField(max_length=45)
    fecha_hora = models.DateTimeField()
    
    def __str__(self):
        return f"Solicitud {self.id} - {self.estado}"
