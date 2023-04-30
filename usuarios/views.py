from tools.global_viewset import GlobalViewSet
from usuarios.models import Usuario
from usuarios.serializers import UsuariosSerializer
from rest_framework.permissions import IsAdminUser


class UsuarioViewSet(GlobalViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuariosSerializer
  search_fields = ['email', 'nome']
  permission_classes = [IsAdminUser]
  