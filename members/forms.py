from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    academic_major = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    car_make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    car_model = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    car_color = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    license_plate = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Driver = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    Rider = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))


    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'academic_major', 'Driver', 'Rider', 'car_make', 'car_model', 'car_color', 'license_plate')