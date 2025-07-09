from django.contrib import admin
from django.urls import path, include
#from apps.adminpanel.admin import admin_site
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Parking API",
      default_version='v1',
      description="API para app de estacionamiento",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #path('grappelli/', include('grappelli.urls')),  # URL para el admin mejorado
    path('admin/', admin.site.urls),
    path('api/authentication/', include('apps.authentication.urls')),
    path('api/parking/', include('apps.parking.urls')),
    path('api/locations/', include('apps.locations.urls')),
    path('api/directions/', include('apps.directions.urls')),
    path('api/', include('apps.session.urls')),
    #path('api/users/', include('apps.users.urls')),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
