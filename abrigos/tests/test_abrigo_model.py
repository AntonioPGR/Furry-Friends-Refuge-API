from abrigos.models import Abrigo
from tools.global_test_model import GlobalModelTestCase
from tools.global_test_view_with_no_auth import GlobalViewSemAuthTestCase


class AbrigoModelTestCase(GlobalModelTestCase):
  
  def test_criacao_de_abrigo_correto(self):
    abrigo_correto = Abrigo(
      nome='abrigo', 
      email='teste@gmail.com', 
      telefone='35992202021', 
      cep='37701242', 
      descricao='um abrigo ae'
    )
    self.espera_salvar_corretamente(abrigo_correto)
    
  def test_criacao_de_abrigo_com_email_incorreto(self):
    abrigo_incorreto = Abrigo(
      nome='abrigo1', 
      email='testegmail.com', 
      telefone='359922021', 
      cep='377012', 
      descricao='um abrigo ae'
    )
    self.espera_erro_de_validacao(abrigo_incorreto)
    
    
class AbrigoViewSemAuthTestCase(GlobalViewSemAuthTestCase):
  fixtures = [
    'fixtures/abrigos.json',
  ]
  
  def setUp(self):
    super().setUp('abrigos')
  
  def test_get_lista_de_abrigos(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_abrigo(self):
    response = self.fazer_requisicao_post({
      'nome': 'abrigo1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_abrigo(self):
    response = self.fazer_requisicao_patch({
      'id': Abrigo.objects.first().id,
      'nome': 'abrigo1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_abrigo(self):
    response = self.fazer_requisicao_put({
      'id': Abrigo.objects.first().id,
      'nome': 'abrigo1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_abrigo(self):
    response = self.fazer_requisicao_put({
      'id': Abrigo.objects.first().id,
    })
    self.espera_resposta_ser_forbidden(response)