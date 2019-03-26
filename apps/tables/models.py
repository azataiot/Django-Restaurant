from django.db import models
from datetime import datetime
from datetime import date
import time
from time import time
# Create your models here.


class Tables(models.Model):
    TABLE_ID = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )
    table_id = models.CharField(choices=TABLE_ID, default='1', max_length=6, verbose_name="Table ID",primary_key=True)
    table_nickname = models.CharField(max_length=50,null=True,blank=True, verbose_name="Table Name")
    table_desc = models.CharField(max_length=200,null=True,blank=True, verbose_name="Table Description")
    # table_occ_date = models.DateField(default=date.today)
    table_occ_start = models.DateTimeField(blank=False, default=datetime.now,verbose_name="Басталу уақыты")
    table_occ_end = models.DateTimeField(blank=False,default=datetime.now, verbose_name="Аяқталу уақыты")
    table_is_available = models.BooleanField(
        default=True,
        )
    add_time =models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Tables"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.table_id