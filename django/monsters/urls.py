from django.urls import path
from . import views

urlpatterns = [
    path('', views.monster_list, name='monster_list'),
]