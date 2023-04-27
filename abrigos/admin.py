from tools.global_admin_page import GlobalAdminPage
from abrigos.models import Abrigo

class AbrigosAdmin(GlobalAdminPage):
  list_display = ['nome', 'email', 'cep']
  list_display_links = ['nome']
  ordering = ['nome']
  search_fields = ['nome']
  
GlobalAdminPage.registerAdminPage(Abrigo, AbrigosAdmin)
