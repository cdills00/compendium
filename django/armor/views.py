from django.shortcuts import render
from .models import Armor

def armor_list(request):
    armor_pieces = Armor.objects.all()
    return render(request, 'armor/armor_list.html', {'armor': armor_pieces})