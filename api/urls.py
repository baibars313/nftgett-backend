from django.urls import path
from .views import *
urlpatterns = [
 path('' ,homepage, name='home' ),
#  path('proxy/' ,proxy, name='proxy' ),
 path('allItems/' ,allItems, name='allItems' ),
# #  api routs
#  path('email/<int:first>/<int:last>/<str:key>/' ,emails, name='user' ),
 path('user/' ,Adduser, name='user' ),
]
# 0300454656