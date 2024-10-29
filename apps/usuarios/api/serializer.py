from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from apps.usuarios.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = Usuarios
        fields = ['id', 'username', 'nombre', 'email', 'telefono', 'tipo_usuario', 'estado', 'password']  
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.password = make_password(password)
        return super().update(instance, validated_data)
