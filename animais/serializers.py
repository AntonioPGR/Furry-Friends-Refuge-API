from rest_framework.serializers import ModelSerializer
from animais.models import Especie, Raca, Animal

class EspeciesSerializer(ModelSerializer):
  class Meta:
    model = Especie
    fields = '__all__'
    read_only_fields = ['id']

  
class RacasSerializer(ModelSerializer):
  class Meta:
    model = Raca
    fields = '__all__'
    depth = 1
    read_only_fields = ['id']

  
class AnimaisSerializer(ModelSerializer):
  class Meta:
    model = Animal
    fields = '__all__'
    depth = 1
    read_only_fields = ['id']
    

  