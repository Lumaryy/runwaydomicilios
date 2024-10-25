from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.domiciliarios.api.view import DomiciliariosViewSet

router_domiciliarios = DefaultRouter()
router_domiciliarios.register('domiciliarios', DomiciliariosViewSet, basename='domiciliarios')

urlpatterns = [
    path('', include(router_domiciliarios.urls)),
]
