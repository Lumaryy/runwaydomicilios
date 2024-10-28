from rest_framework import serializers
from apps.domiciliarios.models import Domiciliarios

class DomiciliariosSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(source='usuarios.nombre', read_only=True)

    class Meta:
        model = Domiciliarios
        fields = ['id', 'usuarios', 'licencia_vehiculo', 'disponibilidad', 'nombre_usuario']  

    def __str__(self):
        return f"Domiciliario: {self.nombre_usuario} ({self.licencia_vehiculo})"
