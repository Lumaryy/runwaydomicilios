from django.contrib import admin
from apps.reportesIncidencia.models import ReportesIncidencia

@admin.register(ReportesIncidencia)
class ReportesIncidenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuarios', 'solicitud', 'tipo_incidencia', 'fecha_reporte', 'short_descripcion')
    list_filter = ('tipo_incidencia', 'fecha_reporte')
    search_fields = ('usuarios__nombre', 'solicitud__id', 'descripcion')
    date_hierarchy = 'fecha_reporte'
    ordering = ('-fecha_reporte',)

    def short_descripcion(self, obj):
        return obj.descripcion[:50]
    short_descripcion.short_description = 'Descripción corta'
