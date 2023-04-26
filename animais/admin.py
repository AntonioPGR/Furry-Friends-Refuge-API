from django.contrib import admin
from animais.models import Animal, Especie, Raca

class AnimalAdmin(admin.ModelAdmin):
  pass
admin.site.register(Animal, AnimalAdmin)

class EspecieAdmin(admin.ModelAdmin):
  pass
admin.site.register(Especie, EspecieAdmin)

class RacaAdmin(admin.ModelAdmin):
  pass
admin.site.register(Raca, RacaAdmin)
