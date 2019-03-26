from django.shortcuts import render
from rest_framework import viewsets
from users.models import UserProfile
from tables.models import Tables
from foods.models import Food,Menu
from cafe.models import SebetModel,Sanat,Tamaq

from .serializers import UserSerializer,TabelSerializer,TamaqSerializer, SanatSerializer, SebetSerializer
# Create your views here.


class UserApiView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class TableApiView(viewsets.ModelViewSet):
    queryset = Tables.objects.all()
    serializer_class = TabelSerializer

class MenuApiView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = TabelSerializer

class FoodApiView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = TabelSerializer

class TamaqApiView(viewsets.ModelViewSet):
    queryset = Tamaq.objects.all()
    serializer_class = TamaqSerializer

class SanatApiView(viewsets.ModelViewSet):
    queryset = Sanat.objects.all()
    serializer_class = SanatSerializer


class SebetApiView(viewsets.ModelViewSet):
    queryset = SebetModel.objects.all()
    serializer_class = SebetSerializer