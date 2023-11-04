from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Refuel(models.Model):
    date = models.DateField()
    odometer = models.IntegerField()
    liters = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    full = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} - {self.odometer} - {self.liters} - {self.price} - {self.full}"