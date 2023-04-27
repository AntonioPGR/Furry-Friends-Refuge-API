from django.core.exceptions import ValidationError
from tools.global_validator import GlobalValidator


opcoes_de_porte = [
  'P', 'M', 'G'
]
class RacaValidator(GlobalValidator):
  @classmethod
  def validar_porte(cls, porte:str):
    if porte not in opcoes_de_porte:
      cls.raise_validation_error('A opção do porte é invalida, favor escolher entre as opções validas!')
    return porte