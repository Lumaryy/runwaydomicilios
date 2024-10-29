from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.api.view import UsuariosViewSet, UserApiGet
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

router_usuarios = DefaultRouter()
router_usuarios.register('usuarios', UsuariosViewSet, basename='usuarios')

urlpatterns = [
    # Rutas de autenticación
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserApiGet.as_view()),
    
    # Rutas de Usuarios
    path('', include(router_usuarios.urls)),
]
