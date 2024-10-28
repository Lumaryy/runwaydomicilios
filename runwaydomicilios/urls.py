from django.contrib import admin
from django.urls import path, include

from apps.solicitud.api.router import router_solicitudes
from apps.domiciliarios.api.router import router_domiciliarios
from apps.reportesIncidencia.api.router import router_reportes_incidencias
from apps.novedades.api.router import router_novedades
from apps.negocios.api.router import router_negocios
from apps.actividad.api.router import router_actividades

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas para los módulos de la API
    path('api/', include('apps.usuarios.api.router')),
    path('api/', include(router_solicitudes.urls)),
    path('api/', include(router_domiciliarios.urls)),
    path('api/', include(router_reportes_incidencias.urls)),
    path('api/', include(router_novedades.urls)),
    path('api/', include(router_negocios.urls)),
    path('api/', include(router_actividades.urls)),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
