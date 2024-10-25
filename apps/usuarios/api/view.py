from rest_framework import viewsets, permissions
from apps.usuarios.api.serializer import UsuariosSerializer
from apps.usuarios.models import Usuarios
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        # Lógica para generar el link de recuperación de contraseña
        return Response({"message": "Password reset link sent"}, status=status.HTTP_200_OK)