from tools.global_validator import GlobalValidator
from datetime import date
from django.core.exceptions import ValidationError

class UsuarioValidator(GlobalValidator):
  @staticmethod
  def validar_usuario_eh_de_maior(nascimento:date):
    if date.today().year - nascimento.year < 18:
      raise ValidationError('Você não pode se cadastrar sendo de menor!')
      
    return nascimento