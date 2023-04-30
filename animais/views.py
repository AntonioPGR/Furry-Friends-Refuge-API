from animais.models import Especie, Raca, Animal
from animais.serializers import EspeciesSerializer, RacasSerializer, AnimaisSerializer
from tools.global_viewset import GlobalViewSet

class EspecieViewSet(GlobalViewSet):
  queryset = Especie.objects.all()
  serializer_class = EspeciesSerializer
  
  
class RacaViewSet(GlobalViewSet):
  queryset = Raca.objects.all()
  serializer_class = RacasSerializer
  filterset_fields = ['porte', 'especie']
  
  
class AnimalViewSet(GlobalViewSet):
  queryset = Animal.objects.all()
  serializer_class = AnimaisSerializer
  filterset_fields = ['sexo', 'status', 'raca', 'abrigo', 'adotado_por']
  
  