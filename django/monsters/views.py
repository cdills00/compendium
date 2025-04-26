from django.shortcuts import render
from .models import Monster

def monster_list(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/monster_list.html', {'monsters': monsters})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Monster
from .forms import MonsterNotesForm

def edit_monster_notes(request, monster_id):
    monster = get_object_or_404(Monster, pk=monster_id)

    if request.method == 'POST':
        form = MonsterNotesForm(request.POST, instance=monster)
        if form.is_valid():
            form.save()
            return redirect('monster_list')  # Redirect somewhere
    else:
        form = MonsterNotesForm(instance=monster)

    return render(request, 'monsters/edit_notes.html', {'form': form, 'monster': monster})