
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('seatselection/',views.selection,name='seatselection'),
    path('register/',views.register,name='register'),
    path('payment/',views.checkout,name='checkout'),
   
    
]
