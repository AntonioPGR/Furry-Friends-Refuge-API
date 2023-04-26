from django.contrib import admin
from abrigos.models import Abrigo

class AbrigosAdmin(admin.ModelAdmin):
  pass
admin.site.register(Abrigo, AbrigosAdmin)
