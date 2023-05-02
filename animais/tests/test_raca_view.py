from animais.models import Raca, Especie
from tools.global_test_view import GlobalViewTestCase

class DefaultRacaViewTestCase:
  fixtures = [
    'fixtures/usuarios.json',
    'fixtures/especie.json',
    'fixtures/racas.json',
  ]
  dados = {
    "nome": "Raca de teste",
    "porte": "P",
    "especie": Especie.objects.first().id
  }
  model = Raca
  url = 'racas'

class RacaViewSemAuthTestCase(DefaultRacaViewTestCase ,GlobalViewTestCase):
  
  def setUp(self):
    super().setUp(url='racas')
    
  def test_get_para_listar_racas(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)

  def test_post_para_criar_raca(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_unauthorized(response)
    
  def test_patch_para_modificar_raca(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_unauthorized(response)
    
  def test_put_para_modificar_raca(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_unauthorized(response)
    
  def test_delete_para_deletar_raca(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_unauthorized(response)
    
    
class RacaViewAutenticadoComoAdmTestCase(DefaultRacaViewTestCase ,GlobalViewTestCase):
  
  def setUp(self):
    super().setUp(url='racas')
    self.autenticar_como_superusuario()
    
  def test_get_para_listar_racas(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)

  def test_post_para_criar_raca(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_created(response)
    
  def test_patch_para_modificar_raca(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_put_para_modificar_raca(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_delete_para_deletar_raca(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_no_content(response)
    

class RacaViewAutenticadoComoUsuarioTestCase(DefaultRacaViewTestCase, GlobalViewTestCase):
  
  def setUp(self):
    super().setUp(url='racas')
    self.autenticar_como_usuario_comum()
    
  def test_get_para_listar_racas(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)

  def test_post_para_criar_raca(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_raca(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_raca(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_raca(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)