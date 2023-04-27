from django.contrib import admin

class GlobalAdminPage(admin.ModelAdmin):
  empty_value_display = "-vazio-"
  list_per_page = 20
  
  @staticmethod
  def registerAdminPage(model_class, admin_class):
    admin.site.register(model_class, admin_class)