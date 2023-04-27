from django.core.exceptions import ValidationError
from datetime import date
from django.core.exceptions import ValidationError


class GlobalValidator:
  @staticmethod
  def validar_nome(nome:str):
    if not nome.isalpha():
      raise ValidationError('São proibidos simbolos e numeros no campo nome')
    return nome
  
  @staticmethod
  def validar_email(email:str):
    if '@' not in email:
      raise ValidationError("O campo de email deve contem '@' !!")
    return email
  
  @staticmethod
  def validar_nascimento(nascimento:date):
    if nascimento > date.today():
      raise ValidationError('A data de nascimento do usuário não pode ser no futuro!')
    return nascimento