from animais.models import Raca, Especie
from tools.global_test_model import GlobalModelTestCase


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
