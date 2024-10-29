from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    class TipoUsuarioChoices(models.TextChoices):
        ADMIN = 'admin', 'Administrador'
        CLIENTE = 'cliente', 'Cliente'
        DOMICILIARIO = 'domiciliario', 'Domiciliario'
        NEGOCIO= 'negocio','Negocio'

    tipo_usuario = models.CharField(
        max_length=15,
        choices=TipoUsuarioChoices.choices,
        default=TipoUsuarioChoices.CLIENTE,
    )

    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)

    class EstadoChoices(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'
    
    estado = models.CharField(
        max_length=10,
        choices=EstadoChoices.choices,
        default=EstadoChoices.ACTIVO,
    )
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.nombre} ({self.tipo_usuario}) - {self.email}"
