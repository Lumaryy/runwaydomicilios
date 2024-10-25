from rest_framework import serializers
from ..models import Solicitudes

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitudes
        fields = ['id', 'punto_recogida', 'punto_entrega', 'descripcion_pedido', 'horario_entrega', 'instrucciones_adicionales', 'estado', 'usuario', 'domiciliario_asignado']
