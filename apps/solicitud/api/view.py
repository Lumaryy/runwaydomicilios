from rest_framework import viewsets, permissions
from apps.solicitud.api.serializer import SolicitudSerializer
from apps.solicitud.models import Solicitud
from apps.domiciliarios.models import Domiciliarios

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        solicitud = serializer.save()
        self.asignar_domiciliario(solicitud)

    def asignar_domiciliario(self, solicitud):
        domiciliario = Domiciliarios.objects.filter(estado='disponible').first()
        if domiciliario:
            solicitud.domiciliario = domiciliario
            solicitud.save()

    def perform_update(self, serializer):
        solicitud = serializer.save()
        if solicitud.novedad_reportada:
            self.reasignar_domiciliario(solicitud)

    def reasignar_domiciliario(self, solicitud):
        nuevo_domiciliario = Domiciliarios.objects.filter(estado='disponible').exclude(id=solicitud.domiciliario.id).first()
        if nuevo_domiciliario:
            solicitud.domiciliario = nuevo_domiciliario
            solicitud.save()
