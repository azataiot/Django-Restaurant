from django.contrib import admin
# Register your models here.
from .models import Tables


class TablesAdmin(admin.ModelAdmin):
    list_display = ['table_id','table_nickname','table_desc','table_is_available','add_time','table_occ_start','table_occ_end']
    search_fields = ['table_id','table_nickname','table_desc','table_is_available','table_occ_start','table_occ_end']
    list_filter = ['table_id','table_nickname','table_desc','table_is_available','add_time','table_occ_start','table_occ_end']
# admin.site.register(Tables,TablesAdmin)