from django.test import TestCase
from animais.models import Raca, Especie

class RacaModelTestCase(TestCase):
  def setUp(self):
    self.especie_default = Especie.objects.create(name='Cachorro')
    self.raca_correta = Raca.objects.create(name='Pastor Alemão', porte='G', especie=self.especie_default)
    self.raca_com_default = Raca.objects.create(name='Pincher', especie=self.especie_default)
    
  def test_raca_criada_corretamente(self):
    self.assertEqual(self.raca_correta.name, 'Pastor Alemão')
    self.assertEqual(self.raca_correta.porte, 'G')
    self.assertEqual(self.raca_correta.especie, self.especie_default)
  
  def test_raca_criaca_com_default(self):
    self.assertEqual(self.raca_com_default.name, 'Pincher')
    self.assertEqual(self.raca_com_default.porte, ('P', 'Pequeno'))
    self.assertEqual(self.raca_com_default.especie, self.especie_default)