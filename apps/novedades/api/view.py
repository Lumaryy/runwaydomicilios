from rest_framework import viewsets, permissions
from apps.negocios.api.serializer import NovedadesSerializer
from apps.novedades.models import Novedades

class NovedadesViewSet(viewsets.ModelViewSet):
    queryset = Novedades.objects.all()
    serializer_class = NovedadesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()