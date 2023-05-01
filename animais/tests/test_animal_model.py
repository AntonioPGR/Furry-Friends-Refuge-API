from animais.models import Animal, Raca
from usuarios.models import Usuario
from abrigos.models import Abrigo
from tools.global_test_model import GlobalModelTestCase 
from datetime import date

class AnimalModelTestCase(GlobalModelTestCase):
  fixtures = [
    'fixtures/especie.json',
    'fixtures/racas.json',
    'fixtures/abrigos.json',
    'fixtures/usuarios.json',
  ]
  
  def test_animal_criado_corretamente(self):
    animal_correto = Animal(
      nome='Charlie Bobinson',
      sexo='M',
      descricao='This is Charlie, a friendly and active dog.',
      status='D',
      foto='path/to/charlie.jpg',
      nascimento=date(2019, 5, 15),
      raca=Raca.objects.first(),
      abrigo=Abrigo.objects.first(),
    )
    self.espera_salvar_corretamente(animal_correto)

  def test_animal_criado_incorretamente(self):
    animal_correto = Animal(
      nome='Charlie123',
      sexo='G',
      descricao='This is Charlie, a friendly and active dog.',
      status='T',
      foto='path/to/charlie.jpg',
      nascimento=date(2030, 5, 15),
      raca=Raca.objects.first(),
      abrigo=Abrigo.objects.first(),
    )
    self.espera_erro_de_validacao(animal_correto)
    