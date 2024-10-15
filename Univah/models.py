from django.db import models

# Create your models here.
class Student(models.Model):

    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)
    email = models.EmailField(null=True)


class Rider(models.Model):

    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)
    CWID = models.CharField(max_length=9, null = True)
    email = models.EmailField(null=True)

class RideRequest(models.Model):
    pickup_location = models.CharField(max_length=255, null = True)
    dropoff_location = models.CharField(max_length = 255, null = True)
    status = models.CharField(max_length = 255, null = True)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='ride_requests')
