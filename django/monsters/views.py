import requests
from django.shortcuts import render

def monster_list(request):
    response = requests.get("https://mhw-db.com/monsters")
    monsters = response.json()[:50]  # Only the first 50
    return render(request, "monsters/monster_list.html", {"monsters": monsters})