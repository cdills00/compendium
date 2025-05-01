from django.urls                 import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.monster_list, name='monster_list'),
    path(
      'monster/<int:monster_id>/edit-notes/',
      login_required(views.edit_monster_notes),
      name='edit_monster_notes'
    ),
]