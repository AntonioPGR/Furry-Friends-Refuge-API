from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from usuarios.validators import UsuarioValidator
from usuarios.managers import UsuarioManager


class Usuario(AbstractBaseUser, PermissionsMixin):
  """
  Representa um usuário cadastrado no sistema.

  Atributos:
  - email: Endereço de e-mail do usuário (obrigatório, único).
  - nome: O nome do usuário (obrigatório, até 30 caracteres).
  - sobrenome: O sobrenome do usuário (obrigatório, até 30 caracteres).
  - nascimento: A data de nascimento do usuário (obrigatória, com validação de idade mínima de 18 anos).
  - is_active: Indica se o usuário está ativo ou não no sistema (padrão é True).
  - is_staff: Indica se o usuário tem permissões de administrador (padrão é False).
  - date_joined: Data de criação da conta do usuário (padrão é a hora atual).
  """
  
  email = models.EmailField(
    unique=True,
    validators=[UsuarioValidator.validar_email]
  )
  nome = models.CharField(
    max_length=30, 
    validators=[UsuarioValidator.validar_nome]
  )
  sobrenome = models.CharField(
    max_length=30,
    validators=[UsuarioValidator.validar_nome]
  )
  nascimento = models.DateField(
    validators=[
      UsuarioValidator.validar_nascimento,
      UsuarioValidator.validar_usuario_eh_de_maior
    ]
  )
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['nome', 'sobrenome', 'nascimento']
  
  objects = UsuarioManager()

  def __str__(self):
    return self.email

  def get_full_name(self):
    return f'{self.nome} {self.sobrenome}'

  def get_short_name(self):
    return self.nome
  
  class Meta:
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'