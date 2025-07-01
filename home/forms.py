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


class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'image', 'category', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Kitob nomi kiriting'
            }),
            'author': forms.Select(attrs={
                'class': 'form-select'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Narxni kiriting'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Kitob haqida qisqacha ma’lumot'
            }),
        }

        
class ExpenceForms(forms.ModelForm): 

    class Meta:
        model = Expence
        fields = ['book', 'price', 'quantity', 'total_price', 'description']
        labels = {
            'book': 'Kitob',
            'price': 'Narx',
            'quantity': 'Soni',
            'total_price': 'Jami narx',
            'description': 'Izoh',
        }
        widgets = {
            'book': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Kitobni tanlang'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Narxni kiriting'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Soni'
            }),
            'total_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'readonly': False,  # Foydalanuvchi o'zgartirmasligi uchun
                
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Qo\'shimcha izoh yozing'
            }),
        }

class SellForms(forms.ModelForm): 

    class Meta:
        model = Sell
        fields = ['book', 'price', 'quantity', 'total_price', 'description']
        labels = {
            'book': 'Kitob',
            'price': 'Narx',
            'quantity': 'Soni',
            'total_price': 'Jami narx',
            'description': 'Izoh',
        }
        widgets = {
            'book': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Kitobni tanlang'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Narxni kiriting'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Soni'
            }),
            'total_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'readonly': False,  # Foydalanuvchi o'zgartirmasligi uchun
                
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Qo\'shimcha izoh yozing'
            }),
        }
        
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['full_name', 'phone_number', 'email', 'birthdate','gender', 'created_at']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'To‘liq ismini kiriting'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqamini kiriting'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email manzilini kiriting'
            }),
            'birthdate': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'created_at': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        
class Staff_paymentForm(forms.ModelForm):
    class Meta:
        model = Staff_payment
        fields = ['staff', 'price', 'created_at']
        widgets = {
            'staff': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'To‘lov summasi',
                'step': '0.01',
                'min': '0'
            }),
            'created_at': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'staff': 'Hodim',
            'price': 'To‘lov miqdori',
            'created_at': 'To‘lov sanasi',
        }