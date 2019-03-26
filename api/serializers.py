
from rest_framework import serializers

from users.models import UserProfile
from tables.models import Tables
from foods.models import Food,Menu
from cafe.models import SebetModel,Sanat,Tamaq

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username','is_staff','nick_name','birthday','gender','address','mobile','is_client','is_client','avatar')

class TabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ('table_id','table_nickname','table_desc','table_is_available','add_time')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('menucategory','menu_name','menu_id','add_time')

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['menu_category','food_name','description','price','food_weight','is_in_cart','add_time']


# sanat

class SanatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanat
        fields = ['id','sanat_aty','add_time']

class TamaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamaq
        fields = ['sanat','aty','salmagi','baga','suret','description','created','updated']

class SebetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SebetModel
        fields = ['nameoo','add_time','updated','foods']