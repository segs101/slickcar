from dataclasses import field
from inspect import trace
from pyexpat import model
from django import forms
# from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Customer

class CustomerForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name =  forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254)

    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'first_name', 'last_name', 'email', 'address', 'phone', 'pix',]