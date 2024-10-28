from django.contrib import admin
from apps.domiciliarios.models import Domiciliarios

@admin.register(Domiciliarios)
class DomiciliariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuarios', 'licencia_vehiculo', 'disponibilidad')
    list_filter = ('disponibilidad',)
    search_fields = ('usuarios__nombre', 'licencia_vehiculo')
    ordering = ('disponibilidad',)

