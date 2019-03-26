from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    BOOL_CHOICE = (
        ('True','True'),
        ("False","False"),
    )
    nick_name = models.CharField(max_length=50, verbose_name="Nick Name", default="", null= True, blank= True)
    birthday = models.DateField(verbose_name="Birth Day", null= True, blank=True)
    gender = models.CharField(choices=GENDER, default='female', max_length=6, verbose_name="Gender")
    address = models.CharField(max_length=100, default="", verbose_name="User Address")
    mobile = models.CharField(max_length=12, verbose_name="Mobile Number", blank=True, null=True)
    avatar = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)
    is_client = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.username


class EmailVerifyRecord(models.Model):
    SEND_TYPE = (
        ('register', 'Registration Verification Code'),
        ('forget', 'Forget Password Verification Code'),
    )
    code = models.CharField(max_length=20, verbose_name= "Verification Code")
    email = models.EmailField(max_length=50, verbose_name="Email")
    send_type = models.CharField(choices=SEND_TYPE, default='register', max_length=8, verbose_name= "Verification Code Type")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="Verification Code Send Time")


    class Meta:
        verbose_name = "Email Verification Code"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    '''
    slides.LunboTu
    '''
    title = models.CharField(max_length=100, verbose_name="Slides")
    image = models.ImageField(upload_to="image/%Y/%m", default="banner/default.png", max_length=100)
    slide_to_url = models.URLField(max_length=200, verbose_name="ULR")
    slide_index = models.IntegerField(default=100, verbose_name="Index of the Slides")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Added Time")


    class Meta:
        verbose_name = "Site Slides"
        verbose_name_plural = verbose_name