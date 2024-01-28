from django.contrib import admin

# Register your models here.

from .models import FuelType, Vehicle, Refuel   

import datetime

from .models import FuelType, Vehicle, Refuel, VehicleImage

@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('fuel_type', 'measurement_unit')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('user','vehicle_name', 'make', 'model', 'year', 'fuel_type')
    search_fields = ('user','vehicle_name', 'make', 'model', 'year', 'fuel_type')
@admin.register(Refuel)
class RefuelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date', 'odometer', 'fuel_amount', 'cost')
    autocomplete_fields = ('vehicle',)
    search_fields = ('vehicle', 'date', 'odometer', 'fuel_amount', 'cost')
    list_filter = ('vehicle', 'date', 'odometer', 'fuel_amount', 'cost')
    fields = ('vehicle', 'date', 'odometer', 'fuel_amount', 'cost')

@admin.register(VehicleImage)
class VehicleImageAdmin(admin.ModelAdmin):
    fields = ('vehicle', 'image')