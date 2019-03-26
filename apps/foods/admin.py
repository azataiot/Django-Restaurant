from django.contrib import admin

# Register your models here.
from .models import Menu,Food

class MenuAdmin(admin.ModelAdmin):
    list_display = ['menucategory','menu_name','menu_id','add_time']
    search_fields =['menucategory','menu_name','menu_id']
    list_filter =['menucategory','menu_name','menu_id','add_time']




class FoodAdmin(admin.ModelAdmin):
    list_display =['menu_category','food_name','description','price','food_weight','is_in_cart','add_time']
    search_fields = ['menu_category','food_name','description','price','food_weight','is_in_cart']
    list_filter = ['menu_category','food_name','description','price','food_weight','is_in_cart','add_time']


# admin.site.register(Menu,MenuAdmin)
# admin.site.register(Food,FoodAdmin)