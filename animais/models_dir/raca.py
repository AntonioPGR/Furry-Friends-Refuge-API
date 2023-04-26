from django.db import models
from animais.validators import RacaValidator
from animais.models_dir.especie import Especie


class Raca(models.Model):
  nome = models.CharField(
    max_length=30, 
    unique=True, 
    blank=False, 
    null=False,
    validators=[RacaValidator.validar_nome]
  )
  porte = models.CharField(
    max_length=1, 
    blank=False, 
    null=False, 
    choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'),],
    default='P',
    validators=[RacaValidator.validar_porte]
  )
  especie = models.ForeignKey(
    to=Especie, 
    on_delete=models.PROTECT, 
    blank=False, 
    null=False
  )
  
  class Meta:
    verbose_name='Raça'
    verbose_name_plural = 'Raças'
    
  def __str__(self):
    return self.nome
    