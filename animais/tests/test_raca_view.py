from animais.models import Raca, Especie
from tools.global_test_view_with_no_auth import GlobalViewSemAuthTestCase

class RacaViewSemAuthTestCase(GlobalViewSemAuthTestCase):
  fixtures = [
    'fixtures/especie.json',
    'fixtures/racas.json'
  ]
  
  def setUp(self):
    super().setUp(url='racas')
    self.dados_da_raca = {
      "nome": "Poodle",
      "porte": "P",
      "especie": Especie.objects.first().id
    }
    
  def test_get_para_listar_racas(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)

  def test_post_para_criar_raca(self):
    response = self.fazer_requisicao_post(self.dados_da_raca)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_raca(self):
    response = self.fazer_requisicao_patch(
      Raca.objects.first().id,
      self.dados_da_raca
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_raca(self):
    response = self.fazer_requisicao_put(
      Raca.objects.first().id,
      self.dados_da_raca
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_raca(self):
    response = self.fazer_requisicao_delete(
      Raca.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)