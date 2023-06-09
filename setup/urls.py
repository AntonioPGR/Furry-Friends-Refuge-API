from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from animais.views import AnimalViewSet, EspecieViewSet, RacaViewSet
from abrigos.views import AbrigoViewSet
from usuarios.views import UsuarioViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
  openapi.Info(
    title="Furry Friends Refuge",
    default_version='v1',
    description="",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="antoninhopgr@gmail.com"),
    license=openapi.License(name="MIT license"),
  ),
  public=True,
  permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='usuarios')
router.register('animais', AnimalViewSet, basename='animais')
router.register('especies', EspecieViewSet, basename='especies')
router.register('racas', RacaViewSet, basename='racas')
router.register('abrigos', AbrigoViewSet, basename='abrigos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=3600), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=3600), name='schema-redoc'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)