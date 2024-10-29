from rest_framework import serializers
from apps.domiciliarios.models import Domiciliarios

class DomiciliariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domiciliarios
        fields = ['id', 'usuarios', 'licencia_vehiculo', 'disponibilidad']

    def __str__(self):
        return f"Domiciliario: {self.nombre_usuario} ({self.licencia_vehiculo})"
