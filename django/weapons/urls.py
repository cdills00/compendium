from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.weapon_list, name='weapon_list'),
    path(
        'weapon/<int:weapon_id>/edit-notes/',
        login_required(views.edit_weapons_notes),
        name='edit_weapons_notes'
    ),
]