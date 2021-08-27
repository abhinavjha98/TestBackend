from django.contrib import admin
from phishing.models import Result,CategoryResult
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class responseAdmin(ImportExportModelAdmin):
    list_display = ('user','url', 'label','date')
    search_fields = ('url', 'label','user')
    list_filter = ('created_at','updated_at','date')

class categoryAdmin(ImportExportModelAdmin):
    list_display = ('url', 'subCategory')
    search_fields = ('url', 'subCategory')
    list_filter = ('created_at','updated_at','url')

admin.site.register(Result,responseAdmin)
admin.site.register(CategoryResult,categoryAdmin)


