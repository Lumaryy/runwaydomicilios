from rest_framework import serializers
from apps.solicitud.models import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id', 'punto_recogida', 'punto_entrega', 'descripcion_pedido', 'horario_entrega', 'instrucciones_adicionales', 'estado', 'usuario', 'domiciliario_asignado']
