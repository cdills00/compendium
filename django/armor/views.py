from django.shortcuts import render, get_object_or_404, redirect
from .models import Armor
from .forms import ArmorNotesForm

def armor_list(request):
    armors = Armor.objects.all()
    return render(request, 'armor/armor_list.html', {'armor': armors})

def edit_armor_notes(request, armor_id):
    armor = get_object_or_404(Armor, pk=armor_id)

    if request.method == 'POST':
        form = ArmorNotesForm(request.POST, instance=armor)
        if form.is_valid():
            form.save()
            return redirect('armor_list')  # Make sure this matches your URL name
    else:
        form = ArmorNotesForm(instance=armor)

    return render(request, 'armor/edit_notes.html', {'form': form, 'armor': armor})