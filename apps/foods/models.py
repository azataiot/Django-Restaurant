from datetime import datetime
from django.db import models

# Create your models here.


class Menu(models.Model):
    MENU_CATEGORY = (
        ('yst', 'Ыстық тамақтар'),
        ('sal', 'Салаттар'),
        ('sor', 'Сорпалар'),
        ('tau', 'Тауық етінен'),
        ('et', 'Етпен жасаған'),
        ('gar', 'Гарнирлер'),
        ('des','Десерттер'),
    )
    MENU_ID = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )

    menucategory = models.CharField(max_length=7, choices=MENU_CATEGORY, default='yst',
                                    verbose_name='Menu Category')
    menu_name = models.CharField(max_length=50,verbose_name='Menu Name')
    menu_id = models.CharField(choices=MENU_ID, default='1', max_length=6, verbose_name="Menu ID")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="Add Time")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.menu_id


#  foods
class Food(models.Model):
    food_name = models.CharField(max_length=200, verbose_name="food name")
    description = models.CharField(max_length=500, blank=True, null=True,verbose_name="Food Description")
    menu_category = models.ForeignKey(Menu,on_delete='CASCAD')
    price = models.IntegerField(default=0,max_length=None,verbose_name="Food Price")
    food_weight = models.IntegerField(default=0,max_length=None,verbose_name="Food Weight")
    is_in_cart = models.BooleanField(
        default=False,verbose_name="Cart Status"
    )
    add_time = models.DateTimeField(default=datetime.now,verbose_name="Add Time")

    class Meta:
        verbose_name = "Foods"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.food_name



