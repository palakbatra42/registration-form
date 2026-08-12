from django import forms
from project.Models.LeadForm import *
from project.Models.LeadStatusHistory import *
from django.forms import ModelForm

class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = "__all__" 

        widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Name'
        }),
        'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        }),
        'phone': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Phone Number'
        }),
        'source': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Source'
        }),
    }
