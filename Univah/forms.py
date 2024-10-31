from django import forms
from . import models

class SigninForm(forms.Form):
    Email = forms.CharField(max_length=20, label="Email")
    Password = forms.CharField(max_length=20, label="Password")

class Bookride(forms.Form):
    pickup_address = forms.CharField(max_length=9, label="pickup_address")
    dropoff_address = forms.CharField(max_length=9, label="dropoff_address")
    
