from rest_framework import serializers
from apps.negocios.models import Negocios

class NegociosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocios
        fields = ['id', 'usuarios', 'nombre', 'banner', 'direccion']  
    def __str__(self):
        return self.nombre
