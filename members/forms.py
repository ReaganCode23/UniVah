from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from Univah.models import Driver, Rider

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=10, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    academic_major = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    vehicle_type = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    vehicle_color = forms.CharField(
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    license_number = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    is_driver = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_rider = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 
                 'phone_number', 'academic_major', 'is_driver', 
                 'is_rider', 'vehicle_type', 'vehicle_color', 
                 'license_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Hide the password field that comes with UserChangeForm
        if self.fields.get('password'):
            self.fields.pop('password')
        
        # Initialize driver fields if user is a driver
        if self.instance:
            try:
                driver = Driver.objects.get(user=self.instance)
                self.fields['is_driver'].initial = True
                self.fields['vehicle_type'].initial = driver.vehicle_type
                self.fields['vehicle_color'].initial = driver.vehicle_color
                self.fields['license_number'].initial = driver.license_number
                self.fields['phone_number'].initial = driver.phone_number
                self.fields['academic_major'].initial = driver.major
            except Driver.DoesNotExist:
                self.fields['is_driver'].initial = False

            # Initialize rider status
            try:
                rider=Rider.objects.get(user=self.instance)
                self.fields['is_rider'].initial = True
                self.fields['phone_number'].initial = rider.phone_number
                self.fields['academic_major'].initial = rider.major
            except Rider.DoesNotExist:
                self.fields['is_rider'].initial = False


    def clean(self):
        cleaned_data = super().clean()
        is_driver = cleaned_data.get('is_driver')
        vehicle_type = cleaned_data.get('vehicle_type')
        vehicle_color = cleaned_data.get('vehicle_color')
        license_number = cleaned_data.get('license_number')
        phone_number = cleaned_data.get('phone_number')
        major = cleaned_data.get('academic_major')



        # If user is a driver, validate vehicle information
        if is_driver:
            if not vehicle_type:
                self.add_error('vehicle_type', 'Vehicle type is required for drivers')
            if not vehicle_color:
                self.add_error('vehicle_color', 'Vehicle color is required for drivers')
            if not license_number:
                self.add_error('license_number', 'License number is required for drivers')

        return cleaned_data