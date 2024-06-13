# forms.py
from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Enter city name', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g., Bengaluru'
    }))
