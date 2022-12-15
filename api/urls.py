from django.urls import path
from .views import *
urlpatterns = [
 path('' ,homepage, name='home' ),
#  path('proxy/' ,proxy, name='proxy' ),
 path('allItems/' ,allItems, name='allItems' ),
# #  api routs
#  path('email/<int:first>/<int:last>/<str:key>/' ,emails, name='user' ),
 path('user/' ,Adduser, name='user' ),
 path('itemids/' ,itemids, name='ids' ),
 path('bid/' ,getBids, name='bids' ),
 path('onsale/' ,allItemsbyaddress, name='onsale' ),
 path('auctions/' ,allItemsauction, name='onsale' ),
 path('license/' ,allItemslicense, name='onsale' ),
]
# 0300454656