from animais.models import Animal, Especie, Raca
from usuarios.models import Usuario
from abrigos.models import Abrigo
from tools.test_global_model import GlobalModelTestCase 
from datetime import date

class AnimalModelTestCase(GlobalModelTestCase):
  
  def test_animal_criado_corretamente(self):
    especie_criada = Especie.objects.create(
      nome='Gataasdadsa'
    )
    raca_criada = Raca.objects.create(
      especie=especie_criada,
      nome='Phenixdasdasd',
      porte='G'
    )
    usuario_criado = Usuario.objects.create(
        email='johndoe@example.com',
        nome='John',
        sobrenome='Doe',
        nascimento='1990-01-01',
        password='050406Ant+',
        is_active=True,
        is_staff=False,
        date_joined='2022-01-01 12:00:00',
    )
    abrigo_criado = abrigo = Abrigo.objects.create(
        nome='Abrigo dos animais',
        foto='',
        email='abrigodosanimais@example.com',
        telefone='11999999999',
        cep='01234567',
        descricao='O Abrigo dos Animais é uma organização sem fins lucrativos que cuida de animais abandonados e maltratados. Nosso objetivo é resgatar, tratar e encontrar lares amorosos para esses animais.'
    )
    animal_correto = Animal(
      nome='Charlie',
      sexo='M',
      descricao='This is Charlie, a friendly and active dog.',
      status='D',
      foto='path/to/charlie.jpg',
      nascimento=date(2019, 5, 15),
      raca=raca_criada,
      abrigo=abrigo_criado,
      adotado_por=usuario_criado
    )
    self.espera_salvar_corretamente(animal_correto)
