from rest_framework import serializers
from ..models import Domiciliarios

class DomiciliariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domiciliarios
        fields = ['id', 'nombre', 'apellidos', 'estado_disponibilidad', 'telefono', 'correo_electronico', 'documento_identidad', 'estado']

