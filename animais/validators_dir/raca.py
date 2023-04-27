from django.core.exceptions import ValidationError
from tools.global_validator import GlobalValidator


opcoes_de_porte = [
  'P', 'M', 'G'
]
class RacaValidator(GlobalValidator):
  @staticmethod
  def validar_porte(porte:str):
    if porte not in opcoes_de_porte:
      raise ValidationError('A opção do porte é invalida, favor escolher entre as opções validas!')
    return porte