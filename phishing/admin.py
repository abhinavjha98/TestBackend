from django.contrib import admin
from phishing.models import Result
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class responseAdmin(ImportExportModelAdmin):
    list_display = ('user','url', 'label','date')
    search_fields = ('url', 'label','user')
    list_filter = ('created_at','updated_at','date')

admin.site.register(Result,responseAdmin)



