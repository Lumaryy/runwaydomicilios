from rest_framework import viewsets, permissions
from apps.reportesIncidencia.api.serializer import ReporteIncidenciasSerializer
from apps.reportesIncidencia.models import ReportesIncidencia

class ReporteIncidenciasViewSet(viewsets.ModelViewSet):
    queryset = ReportesIncidencia.objects.all()
    serializer_class = ReporteIncidenciasSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()