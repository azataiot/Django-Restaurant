from django.db import models
from datetime import datetime
# Create your models here.


class Sanat(models.Model):
    sanat_aty = models.CharField(unique=True,max_length=50, verbose_name="санат атауы", blank=False, null=False, default="Ыстық тамақтар")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Уақыт")

    class Meta:
        verbose_name = "санат"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sanat_aty



class Tamaq(models.Model):
    sanat = models.ForeignKey(Sanat,verbose_name="санат", on_delete=models.CASCADE, related_name="санат")
    aty = models.CharField(unique=True,max_length=50, verbose_name="аты", blank=False, null=False)
    salmagi = models.IntegerField(default=0,verbose_name="салмағы")
    baga = models.IntegerField(default=0,verbose_name="баға")
    suret = models.ImageField(verbose_name="сурет",upload_to="tamaq/%Y/%m/", blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Tamaq"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.aty


class SebetModel(models.Model):
    # session =?
    nameoo = models.CharField(default='sebet',max_length=50, null=True, blank= True, verbose_name="sebet")
    # product = models.ForeignKey(Tamaq, on_delete=models.CASCADE)
    product_sani = models.IntegerField(default=0, verbose_name="Sani")
    foods = models.ManyToManyField(Tamaq,verbose_name="Tamaqtar", blank= True)
    add_time = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Sebet'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nameoo

