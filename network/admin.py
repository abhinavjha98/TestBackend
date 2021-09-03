from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from network.models import TrustedNetwork
# Register your models here.
class TrustedAdmin(ImportExportModelAdmin):
    list_display = ('user','domain','email')
    search_fields = ('user', 'domain')
    list_filter = ('created_at','updated_at','domain')

admin.site.register(TrustedNetwork,TrustedAdmin)