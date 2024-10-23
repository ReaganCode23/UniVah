from django.shortcuts import render, redirect
from django.views import View
from . import models, forms

class Homepage(View):
    def get(self, request):
        form = forms.Bookride()
        drivers = models.Driver.objects.all()
        return render(request, 'univah.html', {'form': form, 'drivers': drivers})
    
    def post(self, request):
        form = forms.Bookride(request.POST)
        drivers = models.Driver.objects.all()
        if form.is_valid():
            first_name = form.cleaned_data['Driver']
            try:
                Driver = models.Driver.objects.get(first_name=first_name)
                Driver.status = "Unavailable"
                Driver.save()
                return render(request, 'ridestatus.html')

            except models.Driver.DoesNotExist:
                return render(request, 'error.html')
        return render(request, 'univah.html', {'form': form, 'drivers': drivers})
            
class SigninPage(View):
    def get(self, request):
        form = forms.SigninForm()
        return render(request, 'login.html')

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

class RideStatus(View):
    def get(self, request):
        return render(request, 'ridestatus.html')