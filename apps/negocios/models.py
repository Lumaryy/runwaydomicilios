from django.db import models
from apps.usuarios.models import Usuarios

class Negocios(models.Model):
    usuarios = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    banner = models.CharField(max_length=255)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"Negocio {self.nombre}"
