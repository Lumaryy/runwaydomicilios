from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.novedades.api.view import NovedadesViewSet

router_novedades = DefaultRouter()
router_novedades.register('novedades', NovedadesViewSet, basename='novedades')

urlpatterns = [
    path('', include(router_novedades.urls)),
]
