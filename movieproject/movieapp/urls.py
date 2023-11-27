
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('list/<pk>',views.index,name='index'),
    path('seatselection/<pk>',views.selection,name='seatselection'),
    path('register/',views.register,name='register'),
    path('checkout/<pk>',views.checkout,name='checkout'),
    path('login/',views.login,name='login'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)