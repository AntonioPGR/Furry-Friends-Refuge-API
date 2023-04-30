from rest_framework.viewsets import ModelViewSet
from animais.models import Especie, Raca, Animal
from animais.serializers import EspeciesSerializer, RacasSerializer, AnimaisSerializer

class EspecieViewSet(ModelViewSet):
  queryset = Especie.objects.all()
  serializer_class = EspeciesSerializer
  search_fields = ['nome']
  ordering = ['nome']
  
  
class RacaViewSet(ModelViewSet):
  queryset = Raca.objects.all()
  serializer_class = RacasSerializer
  filterset_fields = ['porte', 'especie']
  search_fields = ['nome']
  ordering = ['nome']
  
  
class AnimalViewSet(ModelViewSet):
  queryset = Animal.objects.all()
  serializer_class = AnimaisSerializer
  filterset_fields = ['sexo', 'status', 'raca', 'abrigo', 'adotado_por']
  search_fields = ['nome']
  ordering = ['nome']
  
  