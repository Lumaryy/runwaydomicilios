from rest_framework import serializers
from ..models import Negocios

class NegociosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocios
        fields = ['id', 'nombre', 'direccion', 'telefono', 'correo_electronico', 'estado', 'tipo_negocio', 'documento_identidad']

