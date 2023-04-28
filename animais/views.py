from rest_framework.viewsets import ModelViewSet
from animais.models import Especie, Raca, Animal
from animais.serializers import EspeciesSerializer, RacasSerializer, AnimaisSerializer


class EspecieViewSet(ModelViewSet):
  queryset = Especie.objects.all()
  serializer_class = EspeciesSerializer
  
  
class RacaViewSet(ModelViewSet):
  queryset = Raca.objects.all()
  serializer_class = RacasSerializer
  
  
class AnimalViewSet(ModelViewSet):
  queryset = Animal.objects.all()
  serializer_class = AnimaisSerializer