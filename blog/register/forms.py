
from django.forms import ModelForm
from leads.models import Lead
from django import forms
class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = "__all__" 

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'type': 'tel','class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Source'}),
            'status': forms.Select(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], attrs={'class': 'form-control'}),
        }
    