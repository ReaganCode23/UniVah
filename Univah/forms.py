from django import forms
from . import models


class SigninForm(forms.Form):
    Email = forms.CharField(max_length=20, label="Email")
    Password = forms.CharField(max_length=20, label="Password")

from django import forms

class Bookride(forms.Form):
    pickup_address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your pickup location',
            'id': 'pickup'
        })
    )
    dropoff_address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your drop-off location',
            'id': 'dropoff'
        })
    )
    booking_type = forms.ChoiceField(
        choices=[('instant', 'Instant Booking'), ('schedule', 'Schedule Ride')],
        widget=forms.Select(attrs={'id': 'booking_type'})
    )
#Looking back after the expo, we probably could of done a lot of the form logic inside of here instead of in the html file.
#For example, Only submiting the bookride form if the user had no riderequests associated with them
#The html got really cluttered with all of the logic being used in there which I think is due to not using forms.py as much as we should of.