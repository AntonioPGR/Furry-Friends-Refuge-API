from animais.models import Raca, Especie
from tools.test_global_model import GlobalModelTestCase


class RacaModelTestCase(GlobalModelTestCase):
  def test_raca_criada_corretamente(self):
    especie_criada = Especie.objects.create(
      nome='Cachorro'
    )
    raca_correta = Raca(
      especie=especie_criada,
      nome='golden',
      porte='G'
    )
    self.espera_salvar_corretamente(raca_correta)
  
  def test_raca_criada_corretamente(self):
    especie_criada = Especie.objects.create(
      nome='Cachorro'
    )
    raca_incorreta = Raca(
      especie=especie_criada,
      nome='golden',
      porte='G'
    )
    self.espera_erro_de_validacao(raca_incorreta)