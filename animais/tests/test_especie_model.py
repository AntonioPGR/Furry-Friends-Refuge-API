from animais.models import Especie
from tools.global_test_model import GlobalModelTestCase 



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
    