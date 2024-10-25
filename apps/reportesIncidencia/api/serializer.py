from rest_framework import serializers
from apps.reportesIncidencia.models import ReportesIncidencia

class ReporteIncidenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportesIncidencia
        fields = ['id', 'descripcion', 'fecha_reporte', 'usuario', 'solicitud', 'estado']

