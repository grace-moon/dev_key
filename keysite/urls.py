from django.urls import path
from . import views

urlpatterns = [
    path('Win_HWP_key_list/', views.Win_HWP_key_list, name='Win_HWP_keylist'),
    path('Win_Word_key_list/', views.Win_Word_key_list, name='Win_Word_keylist'),
    path('MacOS_HWP_key_list/', views.MacOS_HWP_key_list, name='MacOS_HWP_keylist'),
    path('MacOS_Word_key_list/', views.MacOS_Word_key_list, name='MacOS_Word_keylist'),
    path('',views.home, name='home'),
    path('home2/',views.home2, name='home2'),
]