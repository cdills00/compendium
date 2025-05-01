from django import forms
from .models import Armor

class ArmorNotesForm(forms.ModelForm):
    class Meta:
        model = Armor
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 5, 'cols': 40})
        }