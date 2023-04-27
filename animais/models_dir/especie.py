from django.db import models
from animais.validators import EspecieValidator


class Especie(models.Model):
  """
  Representa uma espécie cadastrada no sistema

  Atributos:
  - nome: o nome da espécie ( obrigatório e unico, com até 30 caracteres )
  """
  
  nome = models.CharField(
    max_length=30, 
    unique=True, 
    blank=False, 
    null=False,
    validators=[EspecieValidator.validar_nome]
  )
  
  class Meta:
    verbose_name='Espécie'
    verbose_name_plural = 'Espécies'
    
  def __str__(self):
    return self.nome