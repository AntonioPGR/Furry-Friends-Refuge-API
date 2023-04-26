from django.db import models
from animais.models import Raca
from abrigos.models import Abrigo
from usuarios.models import Usuario


class Animal(models.Model):
  nome = models.CharField(
    max_length=50, 
    null=False, 
    blank=False
  )
  sexo = models.CharField(
    max_length=1, 
    choices=[('M', 'Masculino'), ('F', 'Feminino')], 
    null=False, 
    blank=False
  )
  descricao = models.TextField(
    blank=True, 
    null=True
  )
  status = models.CharField(
    max_length=20, 
    choices=[('D', 'Disponível para adoção'), ('A', 'Adotado'), ('E', 'Em processo de adoção')],
    default='D', 
    null=False, 
    blank=False
  )
  foto = models.ImageField(
    upload_to='animais_images/%d-%b', 
    null=False, 
    blank=False
  )
  nascimento = models.DateField(
    null=True, 
    blank=True
  )
  entrada_abrigo = models.DateField(
    auto_now_add=True, 
    null=False, 
    blank=False
  )
  raca = models.ForeignKey(
    to=Raca, 
    on_delete=models.PROTECT, 
    null=False, 
    blank=False
  )
  abrigo = models.ForeignKey(
    to=Abrigo, 
    on_delete=models.PROTECT, 
    null=False, 
    blank=False
  )
  adotado_por = models.ForeignKey(
    to=Usuario, 
    on_delete=models.SET_NULL, 
    null=True, 
    blank=True
  )
  
  class Meta:
    verbose_name = 'Animal'
    verbose_name_plural = 'Animais'
    
  def __str__(self):
    return self.nome