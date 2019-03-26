from django.contrib import admin

# Register your models here.
from .models import Sanat,Tamaq,SebetModel


class SanatAdmin(admin.ModelAdmin):
    list_display = ['id','sanat_aty','add_time']
    list_filter = ['id','sanat_aty','add_time']
    search_fields = ['id','sanat_aty']


class TamaqAdmin(admin.ModelAdmin):
    list_display = ['sanat','aty','salmagi','baga','suret','description','created','updated']
    list_filter = ['sanat','aty','salmagi','baga','suret','description','created','updated']
    search_fields = ['sanat','aty','salmagi','baga','suret','description']


class SebetAdmin(admin.ModelAdmin):
    list_display = ['nameoo','add_time','updated']
    list_filter = ['nameoo','add_time','updated']
    search_fields = ['nameoo','foods']



admin.site.register(Sanat,SanatAdmin)
admin.site.register(Tamaq,TamaqAdmin)
admin.site.register(SebetModel,SebetAdmin)