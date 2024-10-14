from django.db import models

# Create your models here.
class Student(models.Model):

    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)
    email = models.EmailField(null=True)


class TechStudent(models.Model):

    first_name = models.CharField(max_length=255, null = True)
    CWID = models.CharField(max_length=9, null = True)
    email = models.EmailField(null=True)
