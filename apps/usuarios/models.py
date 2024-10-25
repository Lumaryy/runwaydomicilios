from django.db import models

class Usuarios(models.Model):
    class TipoUsuarioChoices(models.TextChoices):
        ADMIN = 'admin', 'Administrador'
        CLIENTE = 'cliente', 'Cliente'
        DOMICILIARIO = 'domiciliario', 'Domiciliario'

    tipo_usuario = models.CharField(
        max_length=15,
        choices=TipoUsuarioChoices.choices,
        default=TipoUsuarioChoices.CLIENTE,
    )

    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=255)
    
    class EstadoChoices(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'
    
    estado = models.CharField(
        max_length=10,
        choices=EstadoChoices.choices,
        default=EstadoChoices.ACTIVO,
    )

    def __str__(self):
        return f"{self.nombre} ({self.tipo_usuario}) - {self.email}"
