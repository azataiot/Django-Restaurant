from django.contrib import admin
from .models import Desk,DeskOrder
# Register your models here.

class DeskAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter = ['id','name']
    search_fields = ['id','name']

class DeskOrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','order_date','order_time','client_name','mobile','num_client','table_created','updated']
    list_filter = ['id','name','order_date','order_time','client_name','mobile','num_client','table_created','updated']
    search_fields = ['id','name','client_name','mobile','num_client']


admin.site.register(Desk,DeskAdmin)
admin.site.register(DeskOrder,DeskOrderAdmin)
