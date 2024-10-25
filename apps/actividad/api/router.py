from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.actividad.api.view import ActividadViewSet

router_actividades = DefaultRouter()
router_actividades.register('actividades', ActividadViewSet, basename='actividades')

urlpatterns = [
    path('', include(router_actividades.urls)),
]
