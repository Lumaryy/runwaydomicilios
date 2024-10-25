from django.contrib import admin
from django.urls import path, include



from apps.usuarios.api.router import router_usuarios
from apps.solicitud.api.router import router_solicitudes
from apps.domiciliarios.api.router import router_domiciliarios
from apps.reportesIncidencia.api.router import router_reportes_incidencias
from apps.novedades.api.router import router_novedades
from apps.negocios.api.router import router_negocios
from apps.actividad.api.router import router_actividades



urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas para los módulos de la API
    path('api/', include(router_usuarios.urls)),          
    path('api/', include(router_solicitudes.urls)),      
    path('api/', include(router_domiciliarios.urls)),    
    path('api/', include(router_reportes_incidencias.urls)),      
    path('api/', include(router_novedades.urls)),         
    path('api/', include(router_negocios.urls)),
    path('api/', include(router_actividades.urls))
        
 ]
