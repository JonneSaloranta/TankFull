from .models import Vehicle, Refuel, FuelType, VehicleImage
from django import forms

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RefuelForm(forms.ModelForm):

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    odometer = forms.IntegerField()
    fuel_amount = forms.DecimalField(max_digits=6, decimal_places=2)
    cost = forms.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        model = Refuel
        fields = 'vehicle', 'date', 'odometer', 'fuel_amount', 'cost'


class FuelTypeForm(forms.ModelForm):
    class Meta:
        model = FuelType
        fields = '__all__'


class VehicleImageForm(forms.ModelForm):
    class Meta:
        model = VehicleImage
        fields = '__all__'