from django.contrib import admin
from usuarios.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
  pass
admin.site.register(Usuario, UsuarioAdmin)