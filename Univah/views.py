from django.shortcuts import render
from django.views import View
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from. import forms

# Create your views here.

from django.shortcuts import render, redirect

class Homepage(View):
    def get(self, request):
        return render(request, 'home.html')  # Create a template called new_template.html
    
    def post(self, request):
        if request.method == "POST":
        # Redirect to another URL
            return redirect('login')  # Change '/new-url/' to your desired 
        
        
class SigninPage(View):
    def get(self, request):
        form = forms.SigninForm()
        return render(request, 'login.html', {'form': form})  # Create a template called new_template.html
    
    def post(self, request):

        form = forms.SigninForm(request.POST)

        if form.is_valid():
            cwid = form.cleaned_data['CWID']
            try:
                rider = models.Rider.objects.get(CWID = cwid)
                first_name = rider.first_name
                return render(request, "sucess.html",{'firstname':first_name})
            except models.Rider.DoesNotExist:
                return render(request, "error.html")
            

class BookaRide(View):
    def get (self, request):
        form = forms.BookaRideForm
        return render(request, 'bookride.html', {'form':form})
    
    def post(self, request):
        form = forms.BookaRideForm(request.POST)
        if form.is_valid():
            RideRequest = models.RideRequest(
               dropoff_location = form.cleaned_data['Location']
            )
            try:
                Drivername = form.cleaned_data['Driver']
                Driver = models.Driver.objects.get(first_name=Drivername)
                Driver.status = 'Unavailable'
                Driver.save()
                RideRequest.save()
                return render(request, 'sucess2.html')
            except Driver.DoesNotExist:
                return render(request, 'error.html')
        
    

class GetAllDrivers(View):
    def get(self, request):
        drivers = models.Driver.objects.all()  # Fetch all drivers
        return render(request, 'all_drivers.html', {"drivers": drivers})


class HomeTemplate(View):
    def get(self, request):
        return render(request, 'univah.html')
            