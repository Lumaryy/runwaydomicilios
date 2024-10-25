from django.db import models
from apps.usuarios.models import Usuarios

class Actividad(models.Model):
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.SET_NULL)
    descripcion = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return f"Actividad {self.id} - {self.descripcion[:20]}"
