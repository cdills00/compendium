import requests
from django.shortcuts import render

def weapon_list(request):
    response = requests.get("https://mhw-db.com/weapons")
    weapons = response.json()[:50]  # Only the first 50
    return render(request, "weapons/weapon_list.html", {"weapons": weapons})