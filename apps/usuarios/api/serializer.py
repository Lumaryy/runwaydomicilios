from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from apps.usuarios.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  

    class Meta:
        model = Usuarios
        fields = ['id', 'username', 'nombre', 'email', 'telefono', 'tipo_usuario', 'estado', 'password']
    
    def create(self, validated_data):
        # Cifrar la contraseña antes de crear el usuario
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Si hay una nueva contraseña, cifrarla
        password = validated_data.pop('password', None)
        if password:
            instance.password = make_password(password)

        # Actualizar los demás atributos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
