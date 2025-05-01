from django import forms
from .models import Weapon

class WeaponsNotesForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 5, 'cols': 40})
        }