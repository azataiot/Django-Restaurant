# Generated by Django 2.1.7 on 2019-03-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deskreserve', '0002_deskorder_order_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, null=True, unique=True, verbose_name='үстел'),
        ),
    ]
