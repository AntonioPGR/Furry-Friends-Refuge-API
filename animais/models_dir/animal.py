from django.db import models
from animais.models import Raca
from abrigos.models import Abrigo
from usuarios.models import Usuario
from animais.validators import AnimalValidator


class Animal(models.Model):
  """
    Representa um animal cadastrado no sistema.

    Atributos:
    - nome: O nome do animal (obrigatório, até 50 caracteres).
    - sexo: O sexo do animal (obrigatório, escolha entre: 'masculino' e 'feminino').
    - descricao: Uma descrição breve do animal (opcional).
    - status: O status do animal no abrigo (obrigatório, escolha entre: 'disponível para adoção',  'adotado' e 'em processo de adoção').
    - foto: Uma imagem do animal (obrigatório).
    - nascimento: A data de nascimento do animal (opcional).
    - entrada_abrigo: A data em que o animal entrou no abrigo (obrigatório).
    - raca: A raça do animal (obrigatório, chave estrangeira para a classe Raca).
    - abrigo: O abrigo em que o animal está (obrigatório, chave estrangeira para a classe Abrigo).
    - adotado_por: O usuário que adotou o animal (opcional, chave estrangeira para a classe Usuario).
    """
  
  nome = models.CharField(
    max_length=50, 
    null=False, 
    blank=False,
    validators=[
      AnimalValidator.validar_nome
    ]
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
    blank=True,
    validators=[
      AnimalValidator.validar_nascimento
    ]
  )
  entrada_abrigo = models.DateField(
    auto_now_add=True, 
    null=False, 
    blank=False,
    validators=[
      AnimalValidator.validar_entrada_abrigo
    ]
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
    blank=True,
  )
  
  class Meta:
    verbose_name = 'Animal'
    verbose_name_plural = 'Animais'
    
  def __str__(self):
    return self.nome