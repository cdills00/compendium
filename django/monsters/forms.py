from django import forms
from .models import Monster

class MonsterNotesForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 5, 'cols': 40})
        }