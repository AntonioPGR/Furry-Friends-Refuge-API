from django.db import models
from abrigos.validators import AbrigoValidator


class Abrigo(models.Model):
  nome = models.CharField(
    max_length=30, 
    blank=False, 
    null=False
  )
  foto = models.ImageField(
    upload_to='abrigos_images/%d-%b', 
    default='', 
    null=False, 
    blank=True
  )
  email = models.EmailField(
    max_length=100,
    null=False, 
    blank=False,
    verbose_name='e-mail',
    unique=True,
    validators=[
      AbrigoValidator.validar_email
    ]
  )
  telefone = models.CharField(
    max_length=11, 
    null=False, 
    blank=False,
    unique=True,
    validators= [
      AbrigoValidator.validar_numero_de_celular
    ]
  )
  cep = models.CharField(
    max_length=8, 
    null=False, 
    blank=False, 
    validators= [
      AbrigoValidator.validar_cep
    ]
  )
  descricao = models.TextField(
    max_length=300, 
    null=False, 
    blank=False,
    verbose_name='Descrição'
  )
  
  class Meta:
    verbose_name = 'Abrigo'
    verbose_name_plural = 'Abrigos'

  def __str__(self):
    return self.nome