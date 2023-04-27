import re
from django.core.exceptions import ValidationError
from tools.global_validator import GlobalValidator


class AbrigoValidator(GlobalValidator):
  @classmethod
  def validar_numero_de_celular(cls, numero_de_celular:str):
    formato_correto_do_numero = r'^\d{2}9\d{8}$'
    resultado = re.match(formato_correto_do_numero, numero_de_celular)
    
    if resultado is None:
      cls.raise_validation_error('O numero de celular deve estar no formato: DD9XXXXXXXX')
    return resultado

  @classmethod
  def validar_cep(cls, cep:str):
    formato_correto_cep = r'^\d{8}$'
    resultado = re.match(formato_correto_cep, cep)
    if resultado is None:
      cls.raise_validation_error('O numero de cep deve conter apenas 8 digitos numéricos!!')
    return resultado