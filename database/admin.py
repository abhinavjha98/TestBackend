from django.contrib import admin
from database.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class aa419Admin(ImportExportModelAdmin):
    list_display = ('url', 'label')
    search_fields = ('url', 'label')
    list_filter = ('url', 'label')

class MillionURLAdmin(ImportExportModelAdmin):
    list_display = ('url', 'label')
    search_fields = ('url', 'label')
    list_filter = ('url', 'label')

admin.site.register(aa419,aa419Admin)
admin.site.register(MillionURL,MillionURLAdmin)