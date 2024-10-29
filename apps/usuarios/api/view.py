from rest_framework import viewsets, permissions
from apps.usuarios.api.serializer import UsuariosSerializer
from apps.usuarios.models import Usuarios
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

# Vista para manejar los usuarios
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.AllowAny]  # Permitir acceso sin autenticación para registro

    def perform_create(self, serializer):
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


class UserApiGet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = UsuariosSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

