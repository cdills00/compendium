from django.shortcuts import render, get_object_or_404, redirect
from .models import Weapon
from .forms import WeaponsNotesForm


def weapon_list(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapons/weapon_list.html', {'weapons': weapons})

def edit_weapons_notes(request, weapon_id):
    weapons = get_object_or_404(Weapon, pk=weapon_id)

    if request.method == 'POST':
        form = WeaponsNotesForm(request.POST, instance=weapons)
        if form.is_valid():
            form.save()
            return redirect('weapon_list')  # Make sure this matches your URL name
    else:
        form = WeaponsNotesForm(instance=weapons)

    return render(request, 'armor/edit_notes.html', {'form': form, 'weapons': weapons})