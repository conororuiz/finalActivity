from django.db import models


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=120)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
