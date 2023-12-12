
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('list/<pk>',views.index,name='index'),
    path('seatselection/<pk>',views.selection,name='seatselection'),
    path('checkout/<pk>',views.checkout,name='checkout'),
    path('malayalam/',views.malayalam,name='Malayalam'),
    path('tamil/',views.tamil,name='Tamil'),
    path('hindi/',views.hindi,name='Hindi'),
    path('english/',views.english,name='English'),
    path('kerala/',views.kerala,name='kerala'),
    path('tamilnadu/',views.tamilnadu,name='tamilnadu'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)