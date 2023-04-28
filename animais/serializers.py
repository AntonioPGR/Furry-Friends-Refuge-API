from rest_framework.serializers import ModelSerializer
from animais.models import Especie, Raca, Animal

class EspeciesSerializer(ModelSerializer):
  class Meta:
    model = Especie
    fields = '__all__'

  
class RacasSerializer(ModelSerializer):
  class Meta:
    model = Raca
    fields = '__all__'

  
class AnimaisSerializer(ModelSerializer):
  class Meta:
    model = Animal
    fields = '__all__'

  