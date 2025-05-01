from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.armor_list, name='armor_list'),
    path(
        'armor/<int:armor_id>/edit-notes/',
        login_required(views.edit_armor_notes),
        name='edit_armor_notes'
    ),
]