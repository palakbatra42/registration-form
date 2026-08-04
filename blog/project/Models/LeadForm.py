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

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter Email'}),
        #     'phone': forms.NumberInput(attrs={'type': 'tel','class': 'form-control', 'placeholder': 'Enter Phone Number'}),
        #     'source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Source'}),
        #     'status': forms.Select(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], attrs={'class': 'form-control'}),
        #     'assigned_user': forms.Select( choices=[("Admin", "Admin"),("User", "User")],
        #     attrs={'class': 'form-control'}),
        # }
    