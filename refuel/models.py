from django.db import models
from core.settings import AUTH_USER_MODEL as User

# Create your models here.

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
    date = models.DateField()
    odometer = models.IntegerField()
    fuel_amount = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    units_per_distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.vehicle} - {self.date}'
    
    def save(self, *args, **kwargs):
        self.cost_per_unit = self.cost / self.fuel_amount
        self.units_per_distance = self.fuel_amount / self.odometer
        super(Refuel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.vehicle.save()
        super(Refuel, self).delete(*args, **kwargs)

    def get_driven_distance(self):
        if self.id == 1:
            return 0
        else:
            return self.odometer - Refuel.objects.get(id=self.id-1).odometer

    
    class Meta:
        ordering = ['-date']