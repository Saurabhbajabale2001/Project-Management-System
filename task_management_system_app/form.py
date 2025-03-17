# forms.py
from django import forms
from .models import Leave

class Leave(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['user', 'start_date', 'end_date', 'reason']