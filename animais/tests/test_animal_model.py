from animais.models import Animal, Raca
from usuarios.models import Usuario
from abrigos.models import Abrigo
from tools.global_test_model import GlobalModelTestCase 
from tools.global_test_view import GlobalViewTestCase
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
      nome='Charlie',
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
    

class AnimalViewSemAuthTestCase(GlobalViewTestCase):
  fixtures = [
    'fixtures/animais.json',
    'fixtures/especie.json',
    'fixtures/racas.json',
    'fixtures/abrigos.json',
    'fixtures/usuarios.json',
  ]
  
  def setUp(self):
    super().setUp('animais')
  
  def test_get_lista_de_animais(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_animal(self):
    response = self.fazer_requisicao_post({
      'nome': 'raca1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_animal(self):
    response = self.fazer_requisicao_patch({
      'id': Animal.objects.first().id,
      'nome': 'raca1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_animal(self):
    response = self.fazer_requisicao_put({
      'id': Animal.objects.first().id,
      'nome': 'raca1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_animal(self):
    response = self.fazer_requisicao_put({
      'id': Animal.objects.first().id,
    })
    self.espera_resposta_ser_forbidden(response)