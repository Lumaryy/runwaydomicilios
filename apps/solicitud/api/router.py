from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.solicitud.api.view import SolicitudViewSet

router_solicitudes = DefaultRouter()
router_solicitudes.register('solicitudes', SolicitudViewSet, basename='solicitudes')

urlpatterns = [
    path('', include(router_solicitudes.urls)),
]
