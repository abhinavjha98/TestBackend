from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from account.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserCustomAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'name',
            'mobile',
            'email',
            'dob',
            )}),
    )
    list_display = ('username', 'email', 'name', 'mobile','dob')
    search_fields = ('username', 'name', 'id', 'email')

admin.site.register(User, UserCustomAdmin)
