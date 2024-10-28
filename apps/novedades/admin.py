from django.contrib import admin
from apps.novedades.models import Novedades

@admin.register(Novedades)
class NovedadesAdmin(admin.ModelAdmin):
    list_display = ('id', 'domiciliario', 'solicitud', 'estado', 'fecha_reporte', 'short_descripcion')
    list_filter = ('estado', 'fecha_reporte')
    search_fields = ('domiciliario__usuarios__nombre', 'solicitud__id', 'descripcion')
    date_hierarchy = 'fecha_reporte'
    ordering = ('-fecha_reporte',)

    def short_descripcion(self, obj):
        return obj.descripcion[:50]
    short_descripcion.short_description = 'Descripción corta'

