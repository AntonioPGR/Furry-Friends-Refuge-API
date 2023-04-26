from django.db import models
from animais.validators import EspecieValidator


class Especie(models.Model):
  nome = models.CharField(
    max_length=30, 
    unique=True, 
    blank=False, 
    null=False,
    validators=[EspecieValidator.validar_nome]
  )
  
  class Meta:
    verbose_name='Especie'
    verbose_name_plural = 'Especies'
    
  def __str__(self):
    return self.nome