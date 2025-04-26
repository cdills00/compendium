from django.urls import path
from . import views

urlpatterns = [
    path('', views.monster_list, name='monster_list'),
    path('monster/<int:monster_id>/edit-notes/', views.edit_monster_notes, name='edit_monster_notes'),
]