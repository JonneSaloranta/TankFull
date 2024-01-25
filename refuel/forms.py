from .models import Vehicle, Refuel, FuelType
from django import forms

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RefuelForm(forms.ModelForm):
    class Meta:
        model = Refuel
        fields = '__all__'

class FuelTypeForm(forms.ModelForm):
    class Meta:
        model = FuelType
        fields = '__all__'