from rest_framework.serializers import ModelSerializer
from abrigos.models import Abrigo


class AbrigosSerializer(ModelSerializer):
  class Meta:
    model = Abrigo
    fields = '__all__'
    read_only_fields = ['id']
    