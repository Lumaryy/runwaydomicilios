from django.contrib import admin
from apps.solicitud.models import Solicitud

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuarios', 'domiciliarios', 'direccion_recogida', 'direccion_entrega', 'estado', 'fecha_hora')
    list_filter = ('estado', 'fecha_hora')
    search_fields = ('usuarios__nombre', 'domiciliarios__usuarios__nombre', 'direccion_recogida', 'direccion_entrega')
    date_hierarchy = 'fecha_hora'
    ordering = ('-fecha_hora',)

    def usuario_nombre(self, obj):
        return obj.usuarios.nombre if obj.usuarios else 'Sin usuario'
    usuario_nombre.short_description = 'Usuario'

    def domiciliario_nombre(self, obj):
        return obj.domiciliarios.usuarios.nombre if obj.domiciliarios and obj.domiciliarios.usuarios else 'Sin domiciliario'
    domiciliario_nombre.short_description = 'Domiciliario'
