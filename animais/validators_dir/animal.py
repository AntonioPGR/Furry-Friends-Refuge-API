from tools.global_validator import GlobalValidator
from datetime import date


class AnimalValidator(GlobalValidator):
  @classmethod
  def validar_entrada_abrigo(cls, entrada:date):
    if entrada > date.today():
      cls.raise_validation_error("A data de entrada no abrigo não pode ser no futuro!")
    return entrada