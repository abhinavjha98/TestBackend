from django.contrib import admin
from mail.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class categoryAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at','updated_at')

class mailAdmin(ImportExportModelAdmin):
    list_display = ('user','category')
    search_fields = ('user','category')
    list_filter = ('created_at','updated_at')

class sendMailAdmin(ImportExportModelAdmin):
    list_display = ('subject','category')
    search_fields = ('subject','category')
    list_filter = ('created_at','updated_at')

admin.site.register(Category,categoryAdmin)
admin.site.register(MailUser,mailAdmin)
admin.site.register(SendMail,sendMailAdmin)
# Register your models here.
