from abrigos.models import Abrigo
from abrigos.serializers import AbrigosSerializer
from tools.global_viewset import GlobalViewSet


class AbrigoViewSet(GlobalViewSet):
  queryset = Abrigo.objects.all()
  serializer_class = AbrigosSerializer
  