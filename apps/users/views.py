from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View

# Create your views here.
# Homepage

def HomePageView(request):
    return render(request,'index.html',{})


def MenuView(request):
    return render(request, 'menu.html', {})

def AboutView(request):
    return render(request, 'about.html', {})

def CartView(request):
    return render(request, 'cart.html', {})

class LoginView(View):
    def get(self,request):
        return render(request, "auth-admin.html", {})
    def post(self,request):
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("username", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index-admin.html', {})
        else:
            return render(request, 'auth-admin.html', {"msg": "Пайдаланушы аты немесе пароль дұрыс емес!"})



def StaffBash(request):
    return render(request, 'index-admin.html',{})


def StaffLogoutView(request):
    logout(request)
    return render(request,'auth-admin.html',{'logoutmsg':'Сіз жүйеден шықтыңыз, қайтадан жүйеге кіріңіз!'})

