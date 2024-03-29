from django.db import models
from core.settings import AUTH_USER_MODEL as User
from django.utils import timezone

class FuelType(models.Model):
    fuel_type = models.CharField(max_length=100, primary_key=True, unique=True)
    measurement_unit = models.CharField(max_length=100)

    def __str__(self):
        return self.fuel_type
    

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=100)
    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.vehicle_name}'
    

class Refuel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    odometer = models.IntegerField()
    fuel_amount = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return f'{self.vehicle} - {self.date}'
    
    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        if not self.user:
            self.user = self.vehicle.user
        self.vehicle.save()
        super(Refuel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.vehicle.save()
        super(Refuel, self).delete(*args, **kwargs)
    
    class Meta:
        ordering = ['-date']