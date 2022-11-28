from dataclasses import fields
from django import forms
# from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']