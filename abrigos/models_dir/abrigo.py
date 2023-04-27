from django.db import models
from abrigos.validators import AbrigoValidator


class Abrigo(models.Model):
  """
  Representa um abrigo de animais.

  Atributos:
  - nome: O nome do abrigo (obrigatório, até 30 caracteres).
  - foto: A imagem do abrigo (opcional).
  - email: O endereço de e-mail do abrigo (obrigatório, único, até 100 caracteres).
  - telefone: O número de telefone do abrigo (obrigatório, único, 11 caracteres).
  - cep: O CEP do abrigo (obrigatório, 8 caracteres).
  - descricao: A descrição do abrigo (obrigatório, até 300 caracteres).
  """
  
  nome = models.CharField(
    max_length=30, 
    blank=False, 
    null=False,
    validators=[
      AbrigoValidator.validar_nome
    ]
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