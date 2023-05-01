from abrigos.models import Abrigo
from tools.global_test_view_with_no_auth import GlobalViewSemAuthTestCase


class AbrigoViewSemAuthTestCase(GlobalViewSemAuthTestCase):
  fixtures = [
    'fixtures/abrigos.json',
  ]
  
  def setUp(self):
    super().setUp('abrigos')
    self.dados_do_abrigo = {
      "nome": "Lar dos Animais",
      "foto": "https://amazoniareal.com.br/wp-content/uploads/2022/02/Fotos-arquivo-pessoal-Eliana-Marques-21.jpeg",
      "email": "lardosanimais@gmail.com",
      "telefone": "11988888888",
      "cep": "02002000",
      "descricao": "O Lar dos Animais é um abrigo que cuida de animais abandonados e vítimas de maus tratos. Nosso objetivo é promover a adoção responsável e consciente."
    }
    
  def test_get_lista_de_abrigos(self):
    response = self.fazer_requisicao_get()
    self.espera_resposta_ser_ok(response)
  
  def test_post_para_criar_abrigo(self):
    response = self.fazer_requisicao_post(self.dados_do_abrigo)
    self.espera_resposta_ser_forbidden(response)
    
  def test_patch_para_modificar_abrigo(self):
    response = self.fazer_requisicao_patch(
      Abrigo.objects.first().id,
      self.dados_do_abrigo
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_put_para_modificar_abrigo(self):
    response = self.fazer_requisicao_put(
      Abrigo.objects.first().id,
      self.dados_do_abrigo
    )
    self.espera_resposta_ser_forbidden(response)
    
  def test_delete_para_deletar_abrigo(self):
    response = self.fazer_requisicao_delete(
      Abrigo.objects.first().id
    )
    self.espera_resposta_ser_forbidden(response)