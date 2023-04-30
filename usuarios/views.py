from rest_framework.viewsets import ModelViewSet
from usuarios.models import Usuario
from usuarios.serializers import UsuariosSerializer


class UsuarioViewSet(ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuariosSerializer
  
  filterset_fields = ['is_staff', 'is_active']
  search_fields = ['email', 'nome']
  ordering = ['nome']