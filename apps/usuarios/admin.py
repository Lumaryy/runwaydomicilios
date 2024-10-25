from django.contrib import admin
from .models import Usuarios

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    # Define los campos que se mostrarán en el formulario de administración
    fieldsets = (
        (None, {
            'fields': ('nombre', 'email', 'telefono', 'tipo_usuario', 'estado')
        }),
        ('Contraseña', {
            'fields': ('contrasenia',)  # Considera seguridad para el manejo de contraseñas
        }),
    )

    # Define los campos que se mostrarán en la lista del panel de administración
    list_display = ('nombre', 'email', 'telefono', 'tipo_usuario', 'estado')

    # Define el orden por defecto
    ordering = ('nombre',)

    # Filtros en el panel de administración
    list_filter = ('estado', 'tipo_usuario')

    # Campo de búsqueda
    search_fields = ('nombre', 'email', 'telefono')


