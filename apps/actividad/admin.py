from django.contrib import admin
from apps.actividad.models import Actividad

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'descripcion', 'fecha', 'tipo_actividad')
    list_filter = ('tipo_actividad', 'fecha')
    search_fields = ('descripcion', 'usuario__username', 'tipo_actividad')
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
    
