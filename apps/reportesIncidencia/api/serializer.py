from rest_framework import serializers
from ..models import ReportesIncidencias

class ReporteIncidenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportesIncidencias
        fields = ['id', 'descripcion', 'fecha_reporte', 'usuario', 'solicitud', 'estado']

