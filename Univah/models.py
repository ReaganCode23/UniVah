from django.db import models

class Rider(models.Model):

    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)
    CWID = models.CharField(max_length=9, null = True)
    email = models.EmailField(null=True)

class RideRequest(models.Model):
    pickup_location = models.CharField(max_length=255, null = True)
    dropoff_location = models.CharField(max_length = 255, null = True)

class Driver(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_profile')
    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)
    vehicle_type = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=12, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available')

