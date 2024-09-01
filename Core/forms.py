from django import forms
from .models import *

class SystemInfoForm(forms.ModelForm):
    class Meta:
        model = SystemInformation
        fields = '__all__'
        
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'color_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'color_name'}),
            'color_hex_code': forms.TextInput(attrs={'class': 'form-control', 'type':'color', 'id':'color_hex_code'}),
        }
        
        
class ExpensessTypeCreateForm(forms.ModelForm):
    class Meta:
        model = ExpnsessType
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        }