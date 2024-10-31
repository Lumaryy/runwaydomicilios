from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.solicitud.api.serializer import SolicitudSerializer
from apps.solicitud.models import Solicitud
from apps.domiciliarios.models import Domiciliarios

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    permission_classes = [permissions.AllowAny]

    def asignar_domiciliario(self, solicitud):
        domiciliario = Domiciliarios.objects.filter(estado='disponible').first()
        if domiciliario:
            solicitud.domiciliario = domiciliario
            solicitud.save()



    def reasignar_domiciliario(self, solicitud):
        nuevo_domiciliario = Domiciliarios.objects.filter(estado='disponible').exclude(id=solicitud.domiciliario.id).first()
        if nuevo_domiciliario:
            solicitud.domiciliario = nuevo_domiciliario
            solicitud.save()

    @action(detail=True, methods=['get'], url_path='listar-solicitudes')
    def listar_solicitudes_por_domiciliario(self, request, pk=None):
        """
        listar las solicitudes asignadas a un domiciliario por id.
        """
        try:
            domiciliario = Domiciliarios.objects.get(pk=pk)
            solicitudes = Solicitud.objects.filter(domiciliarios=domiciliario)
            serializer = self.get_serializer(solicitudes, many=True)
            return Response(serializer.data)
        except Domiciliarios.DoesNotExist:
            return Response({"detail": "Domiciliario no encontrado."}, status=404)
