from rest_framework.viewsets import ModelViewSet
from abrigos.models import Abrigo
from abrigos.serializers import AbrigosSerializer


class AbrigoViewSet(ModelViewSet):
  queryset = Abrigo.objects.all()
  serializer_class = AbrigosSerializer
