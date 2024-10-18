from django import forms


class SigninForm(forms.Form):
    CWID = forms.CharField(max_length=9, label="CWID")


class BookaRideForm(forms.Form):
    Location = forms.CharField(max_length=255, label="Location")
    Driver = forms.CharField(max_length=255, label = 'Driver')