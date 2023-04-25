from django.db import models

class Especie(models.Model):
  name = models.CharField(max_length=30, unique=True, blank=False, null=False)


opcoes_de_porte = [
  ('P', 'Pequeno'),
  ('M', 'Médio'),
  ('G', 'Grande'),
]
class Raca(models.Model):
  name = models.CharField(max_length=30, unique=True, blank=False, null=False)
  porte = models.CharField(max_length=1, blank=False, null=False, choices=opcoes_de_porte, default=opcoes_de_porte[0])
  especie = models.ForeignKey(to=Especie, on_delete=models.PROTECT, blank=False, null=False)
  