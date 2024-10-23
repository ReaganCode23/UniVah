from django import forms


class SigninForm(forms.Form):
    CWID = forms.CharField(max_length=9, label="CWID")

class Bookride(forms.Form):
    Driver = forms.CharField(max_length=255, label = 'Driver')