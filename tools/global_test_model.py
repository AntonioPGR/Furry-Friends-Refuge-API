from django.test import TestCase
from django.core.exceptions import ValidationError

class GlobalModelTestCase(TestCase):
  
  def espera_salvar_corretamente(self, model):
    self.validar_model(model)
    model.save()
    
  def espera_erro_de_validacao(self, model):
    with self.assertRaises(ValidationError):
      self.validar_model(model)
      model.save()
    
  def validar_model(self, model):
    model.full_clean()
    