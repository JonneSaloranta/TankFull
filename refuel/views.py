from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

import os
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection
from django.views.decorators.cache import cache_page

from decouple import config
from rest_framework import status

from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from token_auth.token_serializer import UserSerializer
from .serializers import VehicleSerializer, RefuelSerializer, FuelTypeSerializer

from .models import Vehicle, Refuel, FuelType
from .forms import VehicleForm, RefuelForm, FuelTypeForm

from email_login.models import User
from .models import Vehicle, Refuel
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .forms import VehicleForm
import json
from random import randint, uniform

features_list = [
        {
            'name': _('keep-track-title-name'),
            'description': _('keep-track-description-text'),
            'icon': 'bi bi-database'
        },
        {
            'name': _('statistics-title-name'),
            'description': _('statistics-description-text'),
            'icon': 'bi bi-graph-up'
        },
        {
            'name': _('compare-title-name'),
            'description': _('compare-description-text'),
            'icon': 'bi bi-people'
        },
        {
            'name': _('share-title-name'),
            'description': _('share-description-text'),
            'icon': 'bi bi-share'
        },
        {
            'name': _('export-title-name'),
            'description': _('export-description-text'),
            'icon': 'bi bi-file-earmark-arrow-down'
        },
        {
            'name': _('import-title-name'),
            'description': _('import-description-text'),
            'icon': 'bi bi-file-earmark-arrow-up'
        },
        {
            'name': _('token-auth-title-name'),
            'description': _('token-auth-text'),
            'icon': 'bi bi-emoji-sunglasses-fill'
        },
    ]

# @cache_page(60 * 15)
def index(request):
    context = {
        'features': features_list,
    }

    return render(request, 'index.html' , context=context)

def features(request):
    context = {
        'features': features_list
    }

    return render(request, 'features.html', context=context)

@login_required()
def charts(request):
    # TODO: Make this chart work with real data
    data = [uniform(1.6, 2.4) for i in range(12)]
    chart_title = 'Fuel price average per month'
    data_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Serialize data and data_labels to JSON
    data_json = json.dumps(data)
    data_labels_json = json.dumps(data_labels)

    context = {
        'data_json': data_json,
        'chart_title': chart_title,
        'data_labels_json': data_labels_json,
    }
    return render(request, 'charts.html', context=context)

@login_required()
def user_profile(request, user_id):
    if request.user.id != user_id:
        return redirect('refuel:index')

    user = User.objects.filter(id=user_id).first()
    token = Token.objects.filter(user=user).first()
    vehicles = Vehicle.objects.filter(user=user)
    refuels = Refuel.objects.all().order_by('-id')

    context = {
        'user': user,
        'vehicles': vehicles,
        'refuels': refuels,
        'token': token,
    }

    return render(request, 'user_profile.html', context=context)

# TODO: Add authentication to API views and make sure they work

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_vehicles(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    vehicles = Vehicle.objects.filter(user=user)
    serialized_vehicles = VehicleSerializer(vehicles, many=True).data
    return Response({'user': UserSerializer(instance=user).data, 'vehicles': serialized_vehicles}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_vehicle(request):
    vehicleform = VehicleForm(request.data)

    if vehicleform.is_valid():
        # user = models.ForeignKey(User, on_delete=models.CASCADE)
        # vehicle_name = models.CharField(max_length=100)
        # make = models.CharField(max_length=100, null=True, blank=True)
        # model = models.CharField(max_length=100, null=True, blank=True)
        # year = models.IntegerField(null=True, blank=True)
        # fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, blank=True)

        user = get_object_or_404(get_user_model(), id=request.data.get('user_id'))
        vehicle_name = request.data.get('vehicle_name')
        make = request.data.get('make')
        model = request.data.get('model')
        year = request.data.get('year')
        fuel_type = get_object_or_404(FuelType, fuel_type=request.data.get('fuel_type'))

        vehicle = Vehicle.objects.create(user=user, vehicle_name=vehicle_name, make=make, model=model, year=year, fuel_type=fuel_type)
        serialized_vehicle = VehicleSerializer(vehicle).data
        return Response({'user': UserSerializer(instance=user).data, 'vehicle': serialized_vehicle}, status=status.HTTP_200_OK)        
    else:
        return Response({'message': 'Invalid vehicle form'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_vehicle(request):
    vehicle = get_object_or_404(Vehicle, id=request.data.get('vehicle_id'))
    vehicle.delete()
    return Response({'message': 'Vehicle deleted successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_refuel(request):
    user = get_object_or_404(get_user_model(), id=request.data.get('user_id'))
    vehicle = get_object_or_404(Vehicle, id=request.data.get('vehicle_id'))
    refuel = Refuel.objects.create(user=user, vehicle=vehicle, odometer=request.data.get('odometer'), fuel_amount=request.data.get('fuel_amount'), cost=request.data.get('cost'))
    serialized_refuel = RefuelSerializer(refuel).data
    return Response({'user': UserSerializer(instance=user).data, 'vehicle': VehicleSerializer(instance=vehicle).data, 'refuel': serialized_refuel}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_refuel(request):
    refuel = get_object_or_404(Refuel, id=request.data.get('refuel_id'))
    refuel.delete()
    return Response({'message': 'Refuel deleted successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_refuel(request):
    refuel = get_object_or_404(Refuel, id=request.data.get('refuel_id'))
    refuel.odometer = request.data.get('odometer')
    refuel.fuel_amount = request.data.get('fuel_amount')
    refuel.cost = request.data.get('cost')
    refuel.save()
    serialized_refuel = RefuelSerializer(refuel).data
    return Response({'refuel': serialized_refuel}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_vehicle(request):
    vehicle = get_object_or_404(Vehicle, id=request.data.get('vehicle_id'))
    vehicle.vehicle_name = request.data.get('vehicle_name')
    vehicle.save()
    serialized_vehicle = VehicleSerializer(vehicle).data
    return Response({'vehicle': serialized_vehicle}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_refuels(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    refuels = Refuel.objects.filter(user=user)
    serialized_refuels = RefuelSerializer(refuels, many=True).data
    return Response({'user': UserSerializer(instance=user).data, 'refuels': serialized_refuels}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def vehicle_refuels(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    refuels = Refuel.objects.filter(vehicle=vehicle)
    serialized_refuels = RefuelSerializer(refuels, many=True).data
    return Response({'vehicle': VehicleSerializer(instance=vehicle).data, 'refuels': serialized_refuels}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def refuel_details(request, refuel_id):
    refuel = get_object_or_404(Refuel, id=refuel_id)
    serialized_refuel = RefuelSerializer(refuel).data
    return Response({'refuel': serialized_refuel}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def vehicle_details(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    serialized_vehicle = VehicleSerializer(vehicle).data
    return Response({'vehicle': serialized_vehicle}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_details(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_fuel_types(request):
    fuel_types = FuelType.objects.all()
    serialized_fuel_types = FuelTypeSerializer(fuel_types, many=True).data
    return Response({'fuel_types': serialized_fuel_types}, status=status.HTTP_200_OK)