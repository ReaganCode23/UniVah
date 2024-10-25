from django.shortcuts import render, redirect
from django.views import View
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
            extra_notes = form.cleaned_data['extra_notes']

            ride_request = models.RideRequest.objects.create(
                pickup_address=pickup_address,
                dropoff_address=dropoff_address,
                status='Pending',
            )
            return render(request, 'riderhub.html', {'ride_request': ride_request, 'form': form, 'drivers': drivers })

        return render(request, 'riderhub.html', {'form': form, 'drivers': drivers})
