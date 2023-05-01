from abrigos.models import Abrigo
from tools.global_test_view import GlobalViewTestCase


class DefaultAbrigoViewTestCase:
  fixtures = [
    'fixtures/abrigos.json',
    'fixtures/usuarios.json'
  ]
  dados = {
    "nome": "Abrigo de teste",
    "foto": "",
    "email": "abrigodeteste@gmail.com",
    "telefone": "11988883333",
    "cep": "09909900",
    "descricao": "abrigo criado para teste"
  }
  model = Abrigo
  url = 'abrigos'
  
  
class AbrigoViewSemAuthTestCase(DefaultAbrigoViewTestCase, GlobalViewTestCase):
  
  def setUp(self):
    super().setUp(self.url)
    
  def test_get_lista_de_abrigos(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_abrigo(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_abrigo(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_abrigo(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_abrigo(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)
    

class AbrigoViewAutenticadoComoAdmTestCase(DefaultAbrigoViewTestCase, GlobalViewTestCase):
  def setUp(self):
    super().setUp(self.url)
    self.autenticar_como_superusuario()
  
  def test_get_lista_de_abrigos(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_abrigo(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_created(response)
    
  def test_patch_para_modificar_abrigo(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_put_para_modificar_abrigo(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_delete_para_deletar_abrigo(self):
    response = self.fazer_requisicao_delete(self.model.objects.first().id)
    self.espera_resposta_ser_no_content(response)
    

class AbrigoViewAutenticadoComoUsuarioTestCase(DefaultAbrigoViewTestCase, GlobalViewTestCase):
  
  def setUp(self):
    super().setUp(self.url)
    self.autenticar_como_usuario_comum()
  
  def test_get_lista_de_abrigos(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_abrigo(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_abrigo(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_abrigo(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_abrigo(self):
    response = self.fazer_requisicao_delete(self.model.objects.first().id)
    self.espera_resposta_ser_forbidden(response)