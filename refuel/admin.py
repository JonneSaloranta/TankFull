from django.contrib import admin

# Register your models here.

from .models import FuelType, Vehicle, Refuel   

@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('fuel_type', 'measurement_unit')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('user','vehicle_name', 'make', 'model', 'year', 'fuel_type')
    search_fields = ('user','vehicle_name', 'make', 'model', 'year', 'fuel_type')
@admin.register(Refuel)
class RefuelAdmin(admin.ModelAdmin):
    autocomplete_fields = ('vehicle',)