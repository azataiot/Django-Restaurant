from django.db import models
from datetime import datetime, date, time

# Create your models here.


class Desk(models.Model):
    name = models.CharField(max_length=200,default='',unique=True, verbose_name="үстел",blank=True, null=True)

    class Meta:
        verbose_name = "Түскі үстел"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class DeskOrder(models.Model):
    name = models.CharField(unique=True ,max_length=500,default="",verbose_name="Тапсырыс")
    #
    desktop = models.ForeignKey(Desk, on_delete=models.CASCADE)
    # time
    order_date  = models.DateField(default=date.today,verbose_name="Күні")
    order_time = models.TimeField(blank=True, verbose_name="Уақыты")
    order_dt = models.DateTimeField(default=datetime.now)
    # clients
    client_name = models.CharField(max_length=500,default="",verbose_name="Аты-жөні")
    mobile = models.IntegerField(null=True,blank=True)
    num_client = models.IntegerField(default=0)
    table_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Тапсырыс"
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.name
