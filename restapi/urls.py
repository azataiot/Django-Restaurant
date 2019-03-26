"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from users.views import HomePageView,MenuView,AboutView,CartView, LoginView, StaffBash, StaffLogoutView
from orders.views import OrdersView, BronActView
from foods.views import MenusView, FoodsView, EditFoodView
import api.urls as apiurls
from orders.views import BronView, ReservationView
from djreservation import urls as djreservation_urls
# from cafe.views import MyObjectReservation
from cafe.views import ShowMenus, SelectMenu, Sebet
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from deskreserve.views import DeskShow,DeskOrderView, DeskOrderHandle


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apiurls)),
    path('',HomePageView, name = 'index'),
    path('bron/',BronView.as_view(), name = 'bron'),
    path('menu/', ShowMenus, name='menu'),
    path('menu/<int:cat>/',SelectMenu,name ='selectmenu'),
    path('about/', AboutView, name='about'),
    path('cart/', Sebet, name='cart'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',StaffLogoutView, name='logout'),
    path('bash/', StaffBash, name='bash'),
    path('orders/', OrdersView, name='orders'),
    path('menus/', MenusView, name='menus'),
    path('add/', FoodsView, name = 'add'),
    path('bronact/',DeskOrderView,name = 'bronact'),
    path('reservation/',ReservationView.as_view(), name = "reservationold"),
]

# 图片上传的设置
urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
## 图片上传的设置结束
urlpatterns += djreservation_urls.urlpatterns

## urls for deskreserve
urlpatterns += [
    path('desks/',DeskShow,name='reservation'),
    path('success/',DeskOrderHandle, name = 'msgg'),
    path('editfood/',EditFoodView, name = 'editfood')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)