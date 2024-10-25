from rest_framework import serializers
from apps.actividad.models import Actividad

class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id', 'descripcion', 'fecha', 'usuario', 'tipo_actividad']
