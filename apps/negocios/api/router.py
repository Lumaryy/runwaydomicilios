from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.negocios.api.view import NegociosViewSet

router_negocios = DefaultRouter()
router_negocios.register('negocios', NegociosViewSet, basename='negocios')

urlpatterns = [
    path('', include(router_negocios.urls)),
]
