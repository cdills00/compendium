import requests
from django.shortcuts import render

def armor_list(request):
    response = requests.get("https://mhw-db.com/armor")
    armor = response.json()[:50]  # Only the first 50
    return render(request, "armor/armor_list.html", {"armor": armor})