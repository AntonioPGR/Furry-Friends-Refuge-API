from tools.global_test_view import GlobalViewTestCase
from animais.models import Especie

class DefaultEspecieViewTestCase:
  fixtures = [
    'fixtures/usuarios.json',
    'fixtures/especie.json',
  ]
  dados = {
    'nome': 'Galinha'
  }
  model = Especie
  url = 'especies'

class EspecieViewSemAuthTestCase(DefaultEspecieViewTestCase, GlobalViewTestCase):
  
  def setUp(self):
    super().setUp(url='especies')
    
  def test_get_para_listar_especies(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_especie(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_unauthorized(response)
    
  def test_patch_para_modificar_especie(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_unauthorized(response)
    
  def test_put_para_modificar_especie(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_unauthorized(response)
    
  def test_delete_para_deletar_especie(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_unauthorized(response)
    


class EspecieViewAutenticadoComoAdmTestCase(DefaultEspecieViewTestCase, GlobalViewTestCase):
  
  def setUp(self):
    super().setUp(url='especies')
    self.autenticar_como_superusuario()
    
  def test_get_para_listar_especies(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_especie(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_created(response)
    
  def test_patch_para_modificar_especie(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_put_para_modificar_especie(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_delete_para_deletar_especie(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_no_content(response)
    
class EspecieViewAutenticadoComoUsuarioTestCase(DefaultEspecieViewTestCase, GlobalViewTestCase):
  
  def setUp(self):
    super().setUp(url='especies')
    self.autenticar_como_usuario_comum()
    
  def test_get_para_listar_especies(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_especie(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_especie(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_especie(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_especie(self):
    response = self.fazer_requisicao_delete(
      self.model.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)