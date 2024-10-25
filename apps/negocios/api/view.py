from rest_framework import viewsets, permissions
from apps.negocios.api.serializer import NegociosSerializer
from apps.negocios.models import Negocios

class NegociosViewSet(viewsets.ModelViewSet):
    queryset = Negocios.objects.all()
    serializer_class = NegociosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()