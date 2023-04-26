from tools.global_validator import GlobalValidator
from django.core.exceptions import ValidationError


class EspecieValidator(GlobalValidator):
  pass

opcoes_de_porte = [
  ('P', 'Pequeno'),
  ('M', 'Médio'),
  ('G', 'Grande'),
]
class RacaValidator(GlobalValidator):
  
  @staticmethod
  def validar_porte(porte:str):
    if porte not in opcoes_de_porte:
      raise ValidationError('A opção do porte é invalida, favor escolher entre as opções validas!')
    return porte