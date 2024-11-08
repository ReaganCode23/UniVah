from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import models, forms

class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class RiderHub(View):
    def get(self, request):
        #get current user
        user = request.user
        #check if user is loged in
        if user.is_authenticated:
            #check if user is rider
            is_rider = models.Rider.objects.filter(user=user).exists()
            if is_rider:
                #initialize book ride form
                form = forms.Bookride()
                # Retrieve available drivers
                drivers = models.Driver.objects.filter(status='available')
                # Get user's accepted ride requests
                accepted_ride_request = models.RideRequest.objects.filter(rider__user=request.user, status='Accepted').first()
                #Get user's pending ride reqeusts
                ride_request = models.RideRequest.objects.filter(rider__user=request.user, status ='Pending').first()
                #variables to be rendered
                context = {
                    'form': form if not accepted_ride_request else None,
                    'drivers': drivers,
                    'user': request.user,
                    'pending_ride_request': ride_request,
                    'accepted_ride_request': accepted_ride_request,
                }
                return render(request, 'riderhub.html', context)
            #send home if not rider (this would send a message saying "not a registered driver" if we had more time)
            else:
                return redirect('transpo')
        #send to login if not logged in
        else:
            return redirect('login')

    def post(self, request):
        # Handle the ride booking form submission
        form = forms.Bookride(request.POST)
        
        if form.is_valid():
            # Extract data from the form
            pickup_address = form.cleaned_data['pickup_address']
            dropoff_address = form.cleaned_data['dropoff_address']
            booking_type = form.cleaned_data['booking_type'] #this is not used since we did not have time to implement a schedule feature
            
            # Retrieve the user and then get their rider object
            rider = get_object_or_404(models.Rider, user=request.user)
            
            # Create a new ride request
            ride_request = models.RideRequest.objects.create(
                rider=rider,
                pickup_address=pickup_address,
                dropoff_address=dropoff_address,
                booking_type=booking_type,
                status='Pending',  # Initial status
            )
            
            # Redirect to the same page with the new request
            return redirect('riderhub')
        
        # If the form is invalid, re-render the page with the form errors
        drivers = models.Driver.objects.filter(status='available')
        return render(request, 'riderhub.html', {
            'form': form,
            'drivers': drivers,
            'user': request.user,
        })

    def complete_ride(self, request, ride_id):
        # Method to mark a ride as completed
        ride_request = get_object_or_404(models.RideRequest, id=ride_id)
        
        if ride_request.rider.user == request.user and ride_request.status == 'Accepted':
            ride_request.status = 'Completed'  # Mark the ride as completed
            ride_request.save()
        
        return redirect('riderhub')  # Redirect back to the hub


class DriverHub(View):
    def get(self, request):
        #Get the current user
        user = request.user
        #check if user is logged in
        if user.is_authenticated:
            #check if user is driver
            is_driver = models.Driver.objects.filter(user=user).exists()
            if is_driver:
                #get current user's driver object
                driver = models.Driver.objects.get(user=request.user)
                
                #get all pendig ride requests and then only user's active ride requests
                accepted_ride_requests = models.RideRequest.objects.filter(status='Accepted', driver=driver)
                ride_requests = models.RideRequest.objects.filter(status='Pending')
                activedrivers = models.Driver.objects.filter(status = 'Available')

                return render(request, 'driverhub.html', {
                    'accepted_ride_requests': accepted_ride_requests,
                    'pending_ride_requests': ride_requests,
                    'user': request.user,
                    'activedrivers': activedrivers
                })
            
            #redirect home if not a driver
            else:
                return redirect('transpo')
            
        #redirect loggin if not logged in
        else:
            return redirect('login')

    def post(self, request):
        #get riderequest id from accept button
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')
        #get current driver
        driver = models.Driver.objects.get(user=request.user)

        if not request_id:
            return redirect('driverhub')  # Handle gracefully if request_id is missing

        #handle for accept button
        if action == 'Accept':
            # Check if the driver already has an accepted ride request
            if models.RideRequest.objects.filter(driver=driver, status='Accepted').exists():
                messages.error(request, "Ride in progress. Please complete it before accepting another.")
                return redirect('driverhub')

            # Proceed to accept the ride request
            ride_request = get_object_or_404(models.RideRequest, id=request_id)
            ride_request.status = 'Accepted'
            ride_request.driver = driver
            ride_request.save()
            driver.status = 'Unavailable'

        #handle for action button
        elif action == 'Complete':
            # Complete the ride
            ride_request = get_object_or_404(models.RideRequest, id=request_id)
            ride_request.status = 'Completed'
            ride_request.save()

            # Set driver status to available
            driver.status = 'Available'
            driver.save()

        return redirect('driverhub')

            
    
class Transpo(View):
    def get(self, request):
        return render(request, 'transpo-fix.html')
