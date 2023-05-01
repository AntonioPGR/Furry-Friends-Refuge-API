from animais.models import Animal, Raca
from abrigos.models import Abrigo
from tools.global_test_view_with_no_auth import GlobalViewSemAuthTestCase

class AnimalViewSemAuthTestCase(GlobalViewSemAuthTestCase):
  fixtures = [
    'fixtures/animais.json',
    'fixtures/especie.json',
    'fixtures/racas.json',
    'fixtures/abrigos.json',
    'fixtures/usuarios.json',
  ]
  
  def setUp(self):
    super().setUp('animais')
    self.dados_do_animal = {
      "nome": "Branco",
      "sexo": "M",
      "descricao": "Branco é um cachorro dócil e brincalhão, adora passear e correr no parque.",
      "status": "D",
      "foto": "",
      "nascimento": "2019-01-20",
      "entrada_abrigo": "2021-01-10",
      "raca": Raca.objects.first().id,
      "abrigo": Abrigo.objects.first().id
    }
  
  def test_get_lista_de_animais(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_animal(self):
    response = self.fazer_requisicao_post(
      self.dados_do_animal
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_animal(self):
    response = self.fazer_requisicao_patch(
      Animal.objects.first().id,
      self.dados_do_animal
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_animal(self):
    response = self.fazer_requisicao_put(
      Animal.objects.first().id,
      self.dados_do_animal
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_animal(self):
    response = self.fazer_requisicao_delete(
      Animal.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)