from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length =9, null = True)
    CWID = models.CharField(max_length=9, null=True)
    
    class Meta:
        abstract = True

class Rider(UserProfile):
    prefered_drivers = models.CharField(max_length=255, null=True)

class Driver(UserProfile):
    vehicle_type = models.CharField(max_length=50, null = True)
    vehicle_color = models.CharField(max_length=20, null = True)
    license_number = models.CharField(max_length=20, null = True)
    phone_number = models.CharField(max_length=15, null = True)
    status = models.CharField(max_length=12, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RideRequest(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, null = True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    pickup_address = models.CharField(max_length=255, null = True)
    dropoff_address = models.CharField(max_length=255, null = True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], default='Pending')


