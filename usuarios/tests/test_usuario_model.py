from tools.global_test_model import GlobalModelTestCase
from usuarios.models import Usuario
from tools.global_test_view_with_no_auth import GlobalViewSemAuthTestCase


class UsuarioModelTestCase(GlobalModelTestCase):
  
  def setUp(self):
    self.usuario_correto = Usuario.objects.create(
      nome='Antonio',
      sobrenome='Pacheco',
      email='antoninhopgr@gmail.com',
      nascimento='2000-04-05',
      password='050406@Ant+'
    )
    self.usuario_incorreto = Usuario.objects.create(
      nome='Antonio123',
      sobrenome='Pacheco123',
      email='antoninhopgrgmail.com',
      nascimento='2007-04-05',
      password='050406@Ant+'
    )
  
  def test_criacao_de_usuario_correto(self):
    self.espera_salvar_corretamente(self.usuario_correto)
  
  def test_criacao_de_usuario_incorreto(self):
    self.espera_erro_de_validacao(self.usuario_incorreto)
    
  def test_pegar_nome_completo(self):
    self.assertEqual(self.usuario_correto.get_full_name(), 'Antonio Pacheco')
    

class UsuarioViewSemAuthTestCase(GlobalViewSemAuthTestCase):
  fixtures = [
    'fixtures/usuarios.json',
  ]
  
  def setUp(self):
    super().setUp('usuarios')
  
  def test_get_lista_de_usuarios(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_usuario(self):
    response = self.fazer_requisicao_post({
      'nome': 'abrigo1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_usuario(self):
    response = self.fazer_requisicao_patch({
      'id': Usuario.objects.first().id,
      'nome': 'abrigo1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_usuario(self):
    response = self.fazer_requisicao_put({
      'id': Usuario.objects.first().id,
      'nome': 'abrigo1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_usuario(self):
    response = self.fazer_requisicao_put({
      'id': Usuario.objects.first().id,
    })
    self.espera_resposta_ser_forbidden(response)