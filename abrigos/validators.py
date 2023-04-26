import re
from django.core.exceptions import ValidationError
from tools.global_validator import GlobalValidator


class AbrigoValidator(GlobalValidator):
  @staticmethod
  def validar_numero_de_celular(numero_de_celular:str):
    formato_correto_do_numero = r'^\d{2}9\d{8}$'
    resultado = re.match(formato_correto_do_numero, numero_de_celular)
    
    if resultado is None:
      raise ValidationError('O numero de celular deve estar no formato: DD9XXXXXXXX')
    return resultado

  @staticmethod
  def validar_cep(cep:str):
    formato_correto_cep = r'^\d{8}$'
    resultado = re.match(formato_correto_cep, cep)
    if resultado is None:
      raise ValidationError('O numero de cep deve conter apenas 8 digitos numéricos!!')
    return resultado