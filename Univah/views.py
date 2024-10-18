from django.shortcuts import render, redirect
from django.views import View
from . import models, forms

class Homepage(View):
    def get(self, request):
        form = forms.Pickup()
        drivers = models.Driver.objects.all()
        context = {
            'form': form,
            'drivers': drivers
        }
        return render(request, 'univah.html', context)

    def post(self, request):
        form = forms.Pickup(request.POST)
        if form.is_valid():
            RideRequest = models.RideRequest(
                dropoff_location=form.cleaned_data['Location']
            )
            try:
                Drivername = form.cleaned_data['Driver']
                Driver = models.Driver.objects.get(first_name=Drivername)
                Driver.status = 'Unavailable'
                Driver.save()
                RideRequest.save()
                success_message = "Ride request successfully created!"
                context = {
                    'form': forms.Pickup(),  # New empty form
                    'drivers': models.Driver.objects.all(),
                    'success_message': success_message
                }
                return render(request, 'univah.html', context)
            except models.Driver.DoesNotExist:
                error_message = "Driver not found."
                context = {
                    'form': form,
                    'drivers': models.Driver.objects.all(),
                    'error_message': error_message
                }
                return render(request, 'univah.html', context)
        else:
            drivers = models.Driver.objects.all()
            context = {
                'form': form,
                'drivers': drivers
            }
            return render(request, 'univah.html', context)

class SigninPage(View):
    def get(self, request):
        form = forms.SigninForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = forms.SigninForm(request.POST)
        if form.is_valid():
            cwid = form.cleaned_data['CWID']
            try:
                rider = models.Rider.objects.get(CWID=cwid)
                first_name = rider.first_name
                return render(request, "success.html", {'firstname': first_name})
            except models.Rider.DoesNotExist:
                return render(request, "error.html")