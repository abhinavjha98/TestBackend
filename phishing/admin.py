from django.contrib import admin
from phishing.models import Result
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class responseAdmin(ImportExportModelAdmin):
    list_display = ('user','url', 'label')
    search_fields = ('url', 'label')
    list_filter = ('created_at','updated_at')

admin.site.register(Result,responseAdmin)



