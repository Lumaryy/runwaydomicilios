from rest_framework import serializers
from apps.novedades.models import Novedades

class NovedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novedades
        fields = ['id', 'domiciliario', 'solicitud', 'descripcion', 'estado', 'fecha_reporte']  

    def __str__(self):
        return f"Novedad {self.id} - {self.estado}"
