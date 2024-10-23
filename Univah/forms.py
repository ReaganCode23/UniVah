from django import forms
from . import models

class SigninForm(forms.Form):
    CWID = forms.CharField(max_length=9, label="CWID")


class Bookride(forms.Form):
    driver = forms.ModelChoiceField(
        queryset=models.Driver.objects.filter(status='Available'),
        label='Driver',
        empty_label='Select a driver'
    )

    pickup_address = forms.CharField(max_length=9, label="CWID")
    dropoff_address = forms.CharField(max_length=9, label="CWID")
    