from tools.global_validator import GlobalValidator
from datetime import date
from django.core.exceptions import ValidationError

class UsuarioValidator(GlobalValidator):
  @classmethod
  def validar_usuario_eh_de_maior(cls, nascimento:date):
    if date.today().year - nascimento.year < 18:
      cls.raise_validation_error('Você não pode se cadastrar sendo de menor!')
      
    return nascimento