from django.test import TestCase
from animais.models import Especie


class EspecieModelTestCase(TestCase):
  def setUp(self):
    self.especie_correta = Especie(name='Cachorro')
    
  def test_especie_criada_corretamente(self):
    self.assertEqual(self.especie_correta.name, 'Cachorro')
    