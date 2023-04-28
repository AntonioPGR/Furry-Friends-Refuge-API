from tools.global_admin_page import GlobalAdminPage
from usuarios.models import Usuario

class UsuariosAdmin(GlobalAdminPage):
  list_display = ['id', 'email', 'nome', 'nascimento']
  list_display_links = ['nome', 'email']
  ordering = ['email']
  search_fields = ['email']
  
GlobalAdminPage.registerAdminPage(Usuario, UsuariosAdmin)