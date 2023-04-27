from tools.global_admin_page import GlobalAdminPage
from animais.models import Animal, Especie, Raca


class EspecieAdmin(GlobalAdminPage):
  list_display = ['nome']
  list_display_links = ['nome']
  ordering = ['nome']
  search_fields = ['nome']
GlobalAdminPage.registerAdminPage(Especie, EspecieAdmin)

class RacaAdmin(GlobalAdminPage):
  list_display = ['nome', 'porte', 'especie']
  list_display_links = ['nome', 'especie']
  ordering = ['nome']
  search_fields = ['nome', 'especie']
  list_filter = ['porte', 'especie']
GlobalAdminPage.registerAdminPage(Raca, RacaAdmin)

class AnimalAdmin(GlobalAdminPage):
  list_display = ['nome', 'status', 'raca', 'abrigo', 'adotado_por']
  list_display_links = ['nome', 'raca', 'abrigo']
  ordering = ['nome']
  search_fields = ['nome', 'raca', 'abrigo']
  list_filter = ['abrigo', 'raca__especie', 'raca', 'sexo', 'status']
GlobalAdminPage.registerAdminPage(Animal, AnimalAdmin)
