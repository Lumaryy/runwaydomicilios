from django.contrib import admin
from apps.negocios.models import Negocios

@admin.register(Negocios)
class NegociosAdmin(admin.ModelAdmin):
    # Campos a mostrar en el formulario de administración
    fieldsets = (
        (None, {
            'fields': ('usuarios', 'nombre', 'banner', 'direccion')
        }),
    )

    # Campos a mostrar en la lista del panel de administración
    list_display = ('nombre', 'usuarios', 'banner', 'direccion')
    
    # Filtros
    list_filter = ('usuarios',)
    
    # Campo de búsqueda
    search_fields = ('nombre', 'direccion', 'usuarios__nombre')
    
    # Orden por defecto
    ordering = ('nombre',)
