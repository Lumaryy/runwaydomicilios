from rest_framework import serializers
from apps.reportesIncidencia.models import ReportesIncidencia

class ReporteIncidenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportesIncidencia
        fields = ['id', 'usuarios', 'solicitud', 'tipo_incidencia', 'descripcion', 'fecha_reporte'] 

    def __str__(self):
        return f"Reporte {self.id} - {self.descripcion[:20]}"
