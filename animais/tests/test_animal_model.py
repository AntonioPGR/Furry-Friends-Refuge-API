from animais.models import Animal, Especie, Raca
from usuarios.models import Usuario
from abrigos.models import Abrigo
from tools.global_test_model import GlobalModelTestCase 
from datetime import date

class AnimalModelTestCase(GlobalModelTestCase):
  
  def setUp(self):
    self.especie = Especie.objects.create(
      nome='Gato'
    )
    self.raca = Raca.objects.create(
      especie=self.especie,
      nome='Sphenix',
      porte='G'
    )
    self.usuario = Usuario.objects.create(
        email='johndoe@example.com',
        nome='John',
        sobrenome='Doe',
        nascimento='1990-01-01',
        password='050406Ant+'
    )
    self.abrigo = Abrigo.objects.create(
        nome='Abrigo dos animais',
        foto='',
        email='abrigodosanimais@example.com',
        telefone='11999999999',
        cep='37701242',
        descricao='O Abrigo dos Animais é uma organização sem fins lucrativos que cuida de animais abandonados e maltratados. Nosso objetivo é resgatar, tratar e encontrar lares amorosos para esses animais.'
    )
  
  def test_animal_criado_corretamente(self):
    animal_correto = Animal(
      nome='Charlie',
      sexo='M',
      descricao='This is Charlie, a friendly and active dog.',
      status='D',
      foto='path/to/charlie.jpg',
      nascimento=date(2019, 5, 15),
      raca=self.raca,
      abrigo=self.abrigo,
      adotado_por=self.usuario
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
      raca=self.raca,
      abrigo=self.abrigo,
      adotado_por=self.usuario
    )
    self.espera_erro_de_validacao(animal_correto)