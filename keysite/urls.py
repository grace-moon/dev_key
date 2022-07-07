from django.urls import path
from . import views

urlpatterns = [
    path('', views.key_list, name='keylist'),
]