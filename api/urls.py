from django.urls import path,include
# list of users.
# list of foods
# list of the categories
# list of tables

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Users',views.UserApiView)
router.register('Tables',views.TableApiView)
router.register('Menu',views.MenuApiView)
router.register('Tamaq',views.TamaqApiView)
router.register('Sanat',views.SanatApiView)
router.register('Sebet',views.SebetApiView)


urlpatterns = [
    path('',include(router.urls)),
]