from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from apps.usuarios.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'nombre', 'apellidos', 'correo_electronico', 'telefono', 'tipo_documento', 'numero_documento', 'estado', 'rol', 'contrasena']
        extra_kwargs = {
            'contrasena': {'write_only': True}, 
        }

    def create(self, validated_data):
        # Cifra la contraseña antes de guardar el usuario
        validated_data['contrasena'] = make_password(validated_data['contrasena'])
        return super(UsuariosSerializer, self).create(validated_data)

   
    def update(self, instance, validated_data):
        contrasena = validated_data.pop('contrasena', None)
        if contrasena:
            instance.contrasena = make_password(contrasena)
        return super(UsuariosSerializer, self).update(instance, validated_data)
