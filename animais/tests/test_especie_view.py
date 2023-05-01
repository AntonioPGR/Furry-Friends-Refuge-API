from tools.global_test_view_with_no_auth import GlobalViewSemAuthTestCase
from animais.models import Especie


class EspecieViewSemAuthTestCase(GlobalViewSemAuthTestCase):
  fixtures = [
    'fixtures/especie.json',
  ]
  
  def setUp(self):
    super().setUp(url='especies')
    self.dados_da_especie = {
      'nome': 'Cachorro'
    }
    
  def test_get_para_listar_especies(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_especie(self):
    response = self.fazer_requisicao_post(self.dados_da_especie)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_especie(self):
    response = self.fazer_requisicao_patch(
      Especie.objects.first().id,
      self.dados_da_especie
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_especie(self):
    response = self.fazer_requisicao_put(
      Especie.objects.first().id,
      self.dados_da_especie
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_especie(self):
    response = self.fazer_requisicao_delete(
      Especie.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)