from animais.models import Animal, Raca
from abrigos.models import Abrigo
from tools.global_test_view import GlobalViewTestCase

from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

class DefaultAnimalViewTestCase:
  fixtures = [
    'fixtures/animais.json',
    'fixtures/especie.json',
    'fixtures/racas.json',
    'fixtures/abrigos.json',
    'fixtures/usuarios.json',
  ]
  model = Animal
  url = 'animais'
  
  def criar_dados(self):
    self.dados = {
      "nome": "Animal",
      "sexo": "M",
      "descricao": "Branco é um cachorro dócil e brincalhão, adora passear e correr no parque.",
      "status": "D",
      "foto": self.criar_imagem_temporaria(),
      "nascimento": "2019-01-20",
      "entrada_abrigo": "2021-01-10",
      "raca": Raca.objects.first().id,
      "abrigo": Abrigo.objects.first().id
    }
  
  def criar_imagem_temporaria(self):
    bts = BytesIO()
    img = Image.new("RGB", (100, 100))
    img.save(bts, 'jpeg')
    return SimpleUploadedFile("test.jpg", bts.getvalue())


class AnimalViewSemAuthTestCase(DefaultAnimalViewTestCase, GlobalViewTestCase):
  def setUp(self):
    super().setUp('animais')
    super().criar_dados()
  
  def test_get_lista_de_animais(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_animal(self):
    response = self.fazer_requisicao_post(
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_animal(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_animal(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_animal(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)
    

class AnimalViewAutenticadoComoAdmTestCase(DefaultAnimalViewTestCase, GlobalViewTestCase):
  def setUp(self):
    super().setUp('animais')
    super().criar_dados()
    self.autenticar_como_superusuario()
  
  def test_get_lista_de_animais(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_animal(self):
    response = self.fazer_requisicao_post(
      self.dados
    )
    self.espera_resposta_ser_created(response)
    
  def test_patch_para_modificar_animal(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_put_para_modificar_animal(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_delete_para_deletar_animal(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_no_content(response)
    
    
class AnimalViewAutenticadoComoUsuarioTestCase(DefaultAnimalViewTestCase, GlobalViewTestCase):
  def setUp(self):
    super().setUp('animais')
    super().criar_dados()
    self.autenticar_como_usuario_comum
  
  def test_get_lista_de_animais(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_animal(self):
    response = self.fazer_requisicao_post(
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_animal(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_animal(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_animal(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)