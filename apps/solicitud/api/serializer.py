from rest_framework import serializers
from apps.solicitud.models import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = [
            'id', 
            'usuarios', 
            'domiciliarios', 
            'direccion_recogida', 
            'direccion_entrega', 
            'estado', 
            'fecha_hora'
        ]  

    def __str__(self):
        return f"Solicitud {self.id} - {self.estado}"
