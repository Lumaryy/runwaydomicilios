from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from apps.usuarios.api.serializer import UsuariosSerializer
from apps.usuarios.models import Usuarios

# Vista para manejar los usuarios
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.AllowAny]  # Permitir acceso sin autenticación para registro

    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        # Permitir la actualización del estado y otros campos, excepto la contraseña
        if 'password' in serializer.validated_data:
            serializer.validated_data.pop('password')  # Omite la contraseña

        # Guarda los cambios en el usuario
        serializer.save()

# Vista para manejar el inicio de sesión
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Vista para manejar la solicitud de restablecimiento de contraseña
class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        # Lógica para generar el link de recuperación de contraseña
        return Response({"message": "Password reset link sent"}, status=status.HTTP_200_OK)

# Vista para obtener datos del usuario autenticado
class UserApiGet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = UsuariosSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Vista para alternar el estado activo/inactivo del usuario
class ToggleUserStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = get_object_or_404(Usuarios, id=user_id)

        # Cambiar el estado del usuario
        user.estado = 'inactivo' if user.estado == 'activo' else 'activo'  
        user.save()

        status_message = "User activated" if user.estado == 'activo' else "User deactivated"
        return Response({"message": status_message, "new_status": user.estado}, status=status.HTTP_200_OK)
