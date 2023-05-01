from usuarios.models import Usuario
from tools.global_test_view_with_no_auth import GlobalViewSemAuthTestCase


class UsuarioViewSemAuthTestCase(GlobalViewSemAuthTestCase):
  fixtures = [
    'fixtures/usuarios.json',
  ]
  
  def setUp(self):
    super().setUp('usuarios')
    self.dados_de_usuario = {
      'email': 'exemplo@gmail.com',
      'nome': 'exemplo',
      'sobrenome': 'exemplo',
      'password': '12345678',
      'nascimento': '1990-05-20'
    }
  
  def test_get_lista_de_usuarios(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_forbidden(response)
  
  def test_post_para_criar_usuario(self):
    response = self.fazer_requisicao_post(self.dados_de_usuario)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_usuario(self):
    response = self.fazer_requisicao_patch(
      Usuario.objects.first().id, 
      self.dados_de_usuario
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_usuario(self):
    response = self.fazer_requisicao_put(
      Usuario.objects.first().id,
      self.dados_de_usuario
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_usuario(self):
    response = self.fazer_requisicao_delete(Usuario.objects.first().id)
    self.espera_resposta_ser_forbidden(response)
    

class UsuarioViewAutenticadoComoAdmTestCase(GlobalViewSemAuthTestCase):
  fixtures = [
    'fixtures/usuarios.json',
  ]
  
  def setUp(self):
    super().setUp('usuarios')
    usuario = Usuario.objects.get(is_superuser=True)
    self.client.force_authenticate(user=usuario)
    self.dados_de_usuario = {
      'email': 'exemplo@gmail.com',
      'nome': 'exemplo',
      'sobrenome': 'exemplo',
      'password': '12345678',
      'nascimento': '1990-05-20'
    }
  
  def test_get_lista_de_usuarios(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_usuario(self):
    response = self.fazer_requisicao_post(self.dados_de_usuario)
    self.espera_resposta_ser_created(response)
    
  def test_patch_para_modificar_usuario(self):
    response = self.fazer_requisicao_patch(
      Usuario.objects.first().id,
      self.dados_de_usuario
    )
    self.espera_resposta_ser_ok(response)
    
  def test_put_para_modificar_usuario(self):
    response = self.fazer_requisicao_put(
      Usuario.objects.first().id,
      self.dados_de_usuario
    )
    self.espera_resposta_ser_ok(response)
    
  def test_delete_para_deletar_usuario(self):
    response = self.fazer_requisicao_delete(Usuario.objects.first().id)
    self.espera_resposta_ser_no_content(response)