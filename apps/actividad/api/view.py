from rest_framework import viewsets, permissions
from apps.actividad.models import Actividad
from apps.actividad.api.serializer import ActividadesSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
