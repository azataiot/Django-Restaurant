import time
from datetime import datetime,date
from django.db import models
from users.models import UserProfile
from foods.models import Food,Menu
from tables.models import Tables


class TableOrder(models.Model):
    order_id = models.CharField(default=datetime.now().strftime("%Y%m%d%H%M%S"),verbose_name="Тапсырыс ID", max_length=50)
    order_name = models.CharField(max_length=100,default="",null=True,blank=True)
    ordered_tabel = models.ForeignKey(Tables, on_delete="CASCAD")
    order_client_name = models.CharField(max_length=50, verbose_name="Клиенттің атауы")
    order_data = models.DateField(default=date.today,verbose_name="Тапсырыс күні")
    order_time = models.TimeField(default=time.time,verbose_name="Тапсырыс уақыты")
    order_client_mobile = models.IntegerField(verbose_name="телефон нөмірі")
    order_client_number = models.IntegerField(verbose_name="Клиенттің жалпы саны")
    add_time = models.DateTimeField(default=datetime.now)
    order_date = models.DateField(default=datetime.today,verbose_name="брондау күні")
    order_start_time = models.TimeField(blank=True,null=True,verbose_name="Басталу уақыты")
    order_end_time = models.TimeField(blank=True,null=True,verbose_name="Аяқталу уақыты")


    class Meta:
        verbose_name = "Кесте тапсырыстары"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id