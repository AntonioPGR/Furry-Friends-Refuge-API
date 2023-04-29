from rest_framework.serializers import ModelSerializer
from usuarios.models import Usuario

class UsuariosSerializer(ModelSerializer):
  class Meta:
    model = Usuario
    fields = '__all__'
    read_only_fields = ['id']