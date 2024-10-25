from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.reportesIncidencia.api.view import ReporteIncidenciasViewSet

router_reportes_incidencias = DefaultRouter()
router_reportes_incidencias.register('reportes-incidencias', ReporteIncidenciasViewSet, basename='reportes-incidencias')

urlpatterns = [
    path('', include(router_reportes_incidencias.urls)),
]
