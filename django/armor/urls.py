from django.urls import path
from . import views

urlpatterns = [
    path('', views.armor_list, name='armor_list'),
]