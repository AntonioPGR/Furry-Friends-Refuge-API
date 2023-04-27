from django.core.exceptions import ValidationError
from datetime import date
from django.core.exceptions import ValidationError


class GlobalValidator:
  @classmethod
  def validar_nome(cls, nome:str):
    if not nome.isalpha():
      cls.raise_validation_error('São proibidos simbolos e numeros no campo nome')
    return nome
  
  @classmethod
  def validar_email(cls, email:str):
    if '@' not in email:
      cls.raise_validation_error("O campo de email deve contem '@' !!")
    return email
  
  @classmethod
  def validar_nascimento(cls, nascimento:date):
    if nascimento > date.today():
      cls.raise_validation_error('A data de nascimento do usuário não pode ser no futuro!')
    return nascimento

  @staticmethod
  def raise_validation_error(message):
    raise ValidationError(message)