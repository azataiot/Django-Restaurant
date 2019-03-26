from django.contrib import admin
from .models import TableOrder
# Register your models here.




class TableOrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','ordered_tabel','order_client_name','order_data','order_time','order_client_mobile','order_client_number','add_time','order_name']
    search_fields = ['order_id','ordered_tabel','order_client_name','order_data','order_time','order_client_mobile','order_client_number','order_name']
    list_filter = ['order_id','ordered_tabel','order_client_name','order_data','order_time','order_client_mobile','order_client_number','add_time','order_name']


# admin.site.register(TableOrder,TableOrderAdmin)