from django.db import models
from apps.usuarios.models import Usuarios
from apps.solicitud.models import Solicitud  

class ReportesIncidencia(models.Model):
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.SET_NULL)
    solicitud = models.ForeignKey(Solicitud, null=True, on_delete=models.SET_NULL)
    
    class TipoIncidenciaChoices(models.TextChoices):
        TECNICA = 'tecnica', 'Técnica'
        OPERATIVA = 'operativa', 'Operativa'
        LOGISTICA = 'logistica', 'Logística'
    
    tipo_incidencia = models.CharField(
        max_length=20,
        choices=TipoIncidenciaChoices.choices,
        default=TipoIncidenciaChoices.LOGISTICA,
    )
    
    descripcion = models.TextField()
    fecha_reporte = models.DateTimeField()

    def __str__(self):
        return f"Reporte {self.id} - {self.tipo_incidencia}"
