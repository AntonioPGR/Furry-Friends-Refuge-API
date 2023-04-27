from abrigos.models import Abrigo
from tools.test_global_model import GlobalModelTestCase


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
      