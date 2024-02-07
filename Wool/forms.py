from django import forms
from .models import *


class WoolSupplierForm(forms.ModelForm):
    class Meta:
        model = WoolSupplier
        exclude = ['deleted']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WoolSupplierDeleteForm(forms.ModelForm):
    class Meta:
        fields = ['deleted']
        model = WoolSupplier
        widgets = {
            'deleted': forms.HiddenInput()
        }


class WoolSupplierQuantityForm(forms.ModelForm):
    class Meta:
        model = WoolSupplierQuantity
        fields = ['date', 'wool_type', 'wool_company', 'wool_number', 'wool_color', 'wool_weight', 'wool_price', 'total_account']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'type': 'date'}),
            'wool_type': forms.Select(attrs={'class': 'form-control', 'id': 'wool_type'}),
            'wool_company': forms.TextInput(attrs={'class': 'form-control', 'id': 'wool_company'}),
            'wool_number': forms.NumberInput(attrs={'class': 'form-control', 'min':1, 'id': 'wool_number'}),
            'wool_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color', 'id': 'wool_color'}),
            'wool_weight': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'wool_weight'}),
            'wool_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'wool_price'}),
            'total_account': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'total_account', 'readonly': 'readonly'}),
        }


class WoolSupplierPaymentForm(forms.ModelForm):
    class Meta:
        model = WoolSupplierPayment
        fields = ['date', 'value', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'type':'date'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'value'}),
            'reason': forms.TextInput(attrs={'class': 'form-control', 'id': 'reason'}),
        }
