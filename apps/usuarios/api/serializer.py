from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from apps.usuarios.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    contrasena = serializers.CharField(write_only=True)  

    class Meta:
        model = Usuarios
        fields = ['id', 'username', 'nombre', 'email', 'telefono', 'tipo_usuario', 'estado', 'contrasena']  
    def create(self, validated_data):
        contrasena = validated_data.pop('contrasena', None)
        if contrasena:
            validated_data['password'] = make_password(contrasena)
        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        contrasena = validated_data.pop('contrasena', None)
        if contrasena:
            instance.password = make_password(contrasena)
        return super().update(instance, validated_data)
