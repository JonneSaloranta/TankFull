from rest_framework import serializers
from .models import Vehicle, Refuel, FuelType

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RefuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refuel
        fields = '__all__'

class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'