from animais.models import Especie
from tools.global_test_model import GlobalModelTestCase 
from tools.global_test_view import GlobalViewTestCase



class EspecieModelTestCase(GlobalModelTestCase):

  def test_especie_criada_corretamente(self):
    especie_correta = Especie(
      nome='Cachorro'
    )
    self.espera_salvar_corretamente(especie_correta)
  
  def test_especie_criada_incorretamente(self):
    especie_incorreta = Especie(
      nome='AuAu123++'
    )
    self.espera_erro_de_validacao(especie_incorreta)
    

class EspecieViewSemAuthTestCase(GlobalViewTestCase):
  fixtures = [
    'fixtures/especie.json',
  ]
  
  def setUp(self):
    super().setUp(url='especies')
    
  def test_get_para_listar_especies(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_especie(self):
    response = self.fazer_requisicao_post({
      'nome': 'especie1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_especie(self):
    response = self.fazer_requisicao_patch({
      'id': Especie.objects.first().id,
      'nome': 'especie1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_especie(self):
    response = self.fazer_requisicao_put({
      'id': Especie.objects.first().id,
      'nome': 'especie1'
    })
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_especie(self):
    response = self.fazer_requisicao_delete({
      'id': Especie.objects.first().id
    })
    self.espera_resposta_ser_forbidden(response)