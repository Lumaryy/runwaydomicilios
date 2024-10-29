from rest_framework import viewsets, permissions
from apps.domiciliarios.api.serializer import Domiciliarios
from apps.domiciliarios.api.serializer import DomiciliariosSerializer

class DomiciliariosViewSet(viewsets.ModelViewSet):
    queryset = Domiciliarios.objects.all()
    serializer_class = DomiciliariosSerializer


    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
