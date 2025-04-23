from django.shortcuts import render
from .models import Monster

def monster_list(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/monster_list.html', {'monsters': monsters})