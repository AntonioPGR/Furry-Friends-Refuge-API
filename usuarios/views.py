from rest_framework.viewsets import ModelViewSet
from usuarios.models import Usuario
from usuarios.serializers import UsuariosSerializer
from rest_framework.permissions import IsAdminUser


class UsuarioViewSet(ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuariosSerializer
  permission_classes = [IsAdminUser]
  filterset_fields = ['is_staff', 'is_active']
  search_fields = ['email', 'nome']
  ordering = ['nome']