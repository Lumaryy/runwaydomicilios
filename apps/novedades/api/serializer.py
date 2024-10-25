from rest_framework import serializers
from ..models import Novedades

class NovedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novedades
        fields = ['id', 'descripcion', 'fecha_reporte', 'domiciliario', 'estado', 'solicitud']

