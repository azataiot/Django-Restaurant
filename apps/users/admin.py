from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import Group

admin.site.site_title="Ресторан Administration"
admin.site.site_header="Ресторан | Админ-панель"
admin.site.index_title="Админ-панель"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username','mobile','is_staff','last_login','email']
    search_fields = ['username','mobile','is_staff','email']
    list_filter = ['username','mobile','is_staff','last_login','email']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.unregister(Group)
