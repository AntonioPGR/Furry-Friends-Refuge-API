from usuarios.models import Usuario
from tools.global_test_view import GlobalViewTestCase

class DefaultUsuarioViewTestCase:
  fixtures = [
    'fixtures/usuarios.json',
  ]
  dados = {
    'email': 'exemplo@gmail.com',
    'nome': 'exemplo',
    'sobrenome': 'exemplo',
    'password': '12345678',
    'nascimento': '1990-05-20'
  }
  model = Usuario
  url = 'usuarios'

class UsuarioViewSemAuthTestCase(DefaultUsuarioViewTestCase, GlobalViewTestCase):
  def setUp(self):
    super().setUp('usuarios')
  
  def test_get_lista_de_usuarios(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_unauthorized(response)
  
  def test_post_para_criar_usuario(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_unauthorized(response)
    
  def test_patch_para_modificar_usuario(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id, 
      self.dados
    )
    self.espera_resposta_ser_unauthorized(response)
    
  def test_put_para_modificar_usuario(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_unauthorized(response)
    
  def test_delete_para_deletar_usuario(self):
    response = self.fazer_requisicao_delete(self.model.objects.first().id)
    self.espera_resposta_ser_unauthorized(response)
    

class UsuarioViewAutenticadoComoAdmTestCase(DefaultUsuarioViewTestCase, GlobalViewTestCase):
  def setUp(self):
    super().setUp('usuarios')
    self.autenticar_como_superusuario()
  
  def test_get_lista_de_usuarios(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_usuario(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_created(response)
    
  def test_patch_para_modificar_usuario(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_put_para_modificar_usuario(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_ok(response)
    
  def test_delete_para_deletar_usuario(self):
    response = self.fazer_requisicao_delete(self.model.objects.first().id)
    self.espera_resposta_ser_no_content(response)
    

class UsuarioViewAutenticadoComoUsuarioTestCase(DefaultUsuarioViewTestCase, GlobalViewTestCase):
  
  def setUp(self):
    super().setUp('usuarios')
    self.autenticar_como_usuario_comum()
  
  def test_get_lista_de_usuarios(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_forbidden(response)
  
  def test_post_para_criar_usuario(self):
    response = self.fazer_requisicao_post(self.dados)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_usuario(self):
    response = self.fazer_requisicao_patch(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_usuario(self):
    response = self.fazer_requisicao_put(
      self.model.objects.first().id,
      self.dados
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_usuario(self):
    response = self.fazer_requisicao_delete(self.model.objects.first().id)
    self.espera_resposta_ser_forbidden(response)