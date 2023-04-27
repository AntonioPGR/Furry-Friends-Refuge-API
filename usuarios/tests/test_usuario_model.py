from tools.global_test_model import GlobalModelTestCase
from usuarios.models import Usuario


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