from django.contrib.auth.models import User
from django.db import models

#Rider class for users who are registered as riders
class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    major = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=12, null=True)

#Driver class for users who are registered as drivers
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    vehicle_type = models.CharField(max_length=50, null=True)
    vehicle_color = models.CharField(max_length=20, null=True)
    license_number = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    status = models.CharField(max_length=12, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available')
    major = models.CharField(max_length=50, null=True)

#Ride Request class
class RideRequest(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, null=True, related_name='ride_requests')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, related_name='driver_requests')
    pickup_address = models.CharField(max_length=255, null=True)
    dropoff_address = models.CharField(max_length=255, null=True)
    booking_type = models.CharField(max_length=255, null=True) #(not used. no time to implement)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], default='Pending')
