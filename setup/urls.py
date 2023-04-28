from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from animais.views import AnimalViewSet, EspecieViewSet, RacaViewSet
from abrigos.views import AbrigoViewSet
from usuarios.views import UsuarioViewSet

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='usuarios')
router.register('animais', AnimalViewSet, basename='animais')
router.register('especies', EspecieViewSet, basename='especies')
router.register('racas', RacaViewSet, basename='racas')
router.register('abrigos', AbrigoViewSet, basename='abrigos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)