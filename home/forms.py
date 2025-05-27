from django import forms
from .models import *

class AuthorForms(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'birth_date', 'country']

        widgets = {
    'full_name': forms.TextInput(attrs={'class': 'form-control'}),
    'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    'country': forms.TextInput(attrs={'class': 'form-control'}),
}
class ReferenceForms(forms.ModelForm):
    class Meta:
        model = References
        fields = ['type', 'value']
        
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}),
            'value': forms.TextInput(attrs={'class': 'form-control'})
        }
