from usuarios.managers import UsuarioManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from usuarios.validators import UsuarioValidator

class Usuario(AbstractBaseUser, PermissionsMixin):
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