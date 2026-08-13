from django import forms
from project.Models.LeadForm import *
from project.Models.LeadStatusHistory import *
from django.forms import ModelForm


                       
#INPUT VALIDATION
# It is used for:

# taking user input from HTML form
# validating form fields before saving
# adding frontend form widget classes/placeholders
# mapping inputs to the Lead model

class LeadForm(ModelForm):
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if phone is None:
            return phone

        phone = str(phone).strip()

        if not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')

        if len(phone) != 10:
            raise forms.ValidationError('Phone number must be exactly 10 digits.')

        return phone

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
        'phone': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Phone Number',
            'maxlength': '10',
            'pattern': '[0-9]{10}',
            'inputmode': 'numeric',
        }),
        'source': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Source'
        }),
    }
