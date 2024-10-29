from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from . import models, forms

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class RiderHub(View):
    def get(self, request):
        form = forms.Bookride()
        drivers = models.Driver.objects.filter(status='available')
        return render(request, 'riderhub.html', {'form': form, 'drivers': drivers, 'user': request.user})

    def post(self, request):
        form = forms.Bookride(request.POST)
        drivers = models.Driver.objects.filter(status='available')
        if form.is_valid():
            pickup_address = form.cleaned_data['pickup_address']
            dropoff_address = form.cleaned_data['dropoff_address']
            
            rider = get_object_or_404(models.Rider, user=request.user)
            
            ride_request = models.RideRequest.objects.create(
                rider=rider,
                pickup_address=pickup_address,
                dropoff_address=dropoff_address,
                status='Pending',
            )
            return render(request, 'riderhub.html', {'ride_request': ride_request, 'form': form, 'drivers': drivers, 'user': request.user})
        return render(request, 'riderhub.html', {'form': form, 'drivers': drivers})

class DriverHub(View):
    def get(self, request):
        ride_requests = models.RideRequest.objects.filter(driver=None, status='Pending')  # Only show pending requests
        return render(request, 'driverhub.html', {'ride_requests': ride_requests})
    
class Transpo(View):
    def get(self, request):
        return render(request, 'transpo-fix.html')