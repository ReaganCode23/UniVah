#The members app was created with the help of the youtuber codemy.com and his Django turorial videos
#https://www.youtube.com/@Codemycom

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditProfileForm
from django.contrib.auth.models import Group
from Univah.models import Driver, Rider
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('login')
    

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('transpo')
            # Redirect to a success page.
                
        else:
            messages.success(request, ("There Was an Error Logging In, Try Again..."))
            # Return an 'invalid login' error message.
            return redirect('login')
    return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('transpo')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('transpo')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        try:
            user = form.save(commit=False)
            
            # Handle driver status and details
            if form.cleaned_data.get('is_driver', False):
                # Get or create the driver instance
                driver, created = Driver.objects.get_or_create(user=user)
                
                # Update driver details
                driver.vehicle_type = form.cleaned_data.get('vehicle_type', '')
                driver.vehicle_color = form.cleaned_data.get('vehicle_color', '')
                driver.license_number = form.cleaned_data.get('license_number', '')
                driver.phone_number = form.cleaned_data.get('phone_number', '')
                driver.major = form.cleaned_data.get('academic_major')

                
                # Save the driver instance
                driver.save()
                
                # Print for debugging
                print(f"Updated driver details: Type={driver.vehicle_type}, Color={driver.vehicle_color}, License={driver.license_number}")
            else:
                # If user unchecks driver status, delete their driver record
                Driver.objects.filter(user=user).delete()
            
            # Handle rider status
            if form.cleaned_data.get('is_rider', False):
                rider, created = Rider.objects.get_or_create(user=user)
                rider.major = form.cleaned_data.get('academic_major')
                rider.save()
            else:
                Rider.objects.filter(user=user).delete()
            
            # Save the user instance
            user.save()
            form.save_m2m()  # Save many-to-many relationships if any
            
            messages.success(self.request, "Profile updated successfully!")
            return super().form_valid(form)
            
        except Exception as e:
            print(f"Error updating profile: {str(e)}")  # Print for debugging
            messages.error(self.request, f"Error updating profile: {str(e)}")
            return self.form_invalid(form)