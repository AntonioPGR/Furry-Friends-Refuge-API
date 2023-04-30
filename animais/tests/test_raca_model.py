from animais.models import Raca, Especie
from tools.global_test_model import GlobalModelTestCase
from tools.global_test_view import GlobalViewTestCase


class RacaModelTestCase(GlobalModelTestCase):
  fixtures = ['fixtures/especie.json', ]
  
  def test_raca_criada_corretamente(self):
    raca_correta = Raca(
      especie=Especie.objects.first(),
      nome='golden',
      porte='G'
    )
    self.espera_salvar_corretamente(raca_correta)
    
  def test_raca_criada_incorretamente(self):
    raca_correta = Raca(
      especie=Especie.objects.first(),
      nome='golden',
      porte='Grande'
    )
    self.espera_erro_de_validacao(raca_correta)


class RacaViewSemAuthTestCase(GlobalViewTestCase):
  fixtures = [
    'fixtures/especie.json',
    'fixtures/racas.json'
  ]
  
  def setUp(self):
    super().setUp(url='racas')
    
  def test_get_para_listar_racas(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_raca(self):
    response = self.fazer_requisicao_post({
      'nome': 'raca1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_raca(self):
    response = self.fazer_requisicao_patch({
      'id': Raca.objects.first().id,
      'nome': 'raca1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_raca(self):
    response = self.fazer_requisicao_put({
      'id': Raca.objects.first().id,
      'nome': 'raca1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_raca(self):
    response = self.fazer_requisicao_put({
      'id': Raca.objects.first().id,
    })
    self.espera_resposta_ser_forbidden(response)