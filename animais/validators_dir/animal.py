from tools.global_validator import GlobalValidator
from datetime import date
from django.core.exceptions import ValidationError


class AnimalValidator(GlobalValidator):
  @staticmethod
  def validar_entrada_abrigo(entrada:date):
    if entrada > date.today():
      raise ValidationError("A data de entrada no abrigo não pode ser no futuro!")
    return entrada