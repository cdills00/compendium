from django.shortcuts import render
from .models import Weapon

def weapon_list(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapons/weapon_list.html', {'weapons': weapons})