from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

import os
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection, message
from django.views.decorators.cache import cache_page
from django.contrib import messages

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

from .models import Vehicle, Refuel, FuelType, VehicleImage
from .forms import VehicleForm, RefuelForm, FuelTypeForm, VehicleImageForm

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


def map(request):
    return render(request, 'map.html')

@login_required()
def charts(request):
    # TODO: Make this chart work with real data
    data = [uniform(1.6, 2.4) for i in range(12)]
    chart_title = _('Fuel price average per month')
    data_labels = [_('January'), _('February'), _('March'), _('April'), _('May'), _('June'), _('July'), _('August'), _('September'), _('October'), _('November'), _('December')]

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
    user_vehicles = Vehicle.objects.filter(user=user)
    refuels = Refuel.objects.all().order_by('-id')
    vehicle_images = VehicleImage.objects.all().order_by('-id')

    context = {
        'user': user,
        'user_vehicles': user_vehicles,
        'refuels': refuels,
        'token': token,
        'vehicle_images': vehicle_images,
    }

    return render(request, 'user_profile.html', context=context)


@login_required()
def vehicle_details(request, vehicle_id):

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.POST:
        form = RefuelForm(request.POST)
        if form.is_valid():
            refuel = form.save(commit=False)
            refuel.vehicle = get_object_or_404(Vehicle, id=vehicle_id)
            refuel.save()
            messages.success(request, _('Refuel added successfully'))
            return redirect('refuel:vehicle_details', vehicle_id=vehicle_id)
        else:
            messages.error(request, _('Invalid refuel form'))
            messages.error(request, form.errors)
            return redirect('refuel:vehicle_details', vehicle_id=vehicle_id)

    user_vehicles = Vehicle.objects.filter(user=request.user)

    try:
        last_refuel = Refuel.objects.filter(vehicle=vehicle).order_by('-id').first()
    except Refuel.DoesNotExist:
        last_refuel = None

    form = RefuelForm()

    # Retrieve refueling data related to this vehicle
    refuels = Refuel.objects.filter(vehicle=vehicle).order_by('-id')

    data = [uniform(1.6, 2.4) for i in range(12)]
    chart_title = _('Fuel price average per month')
    data_labels = [_('January'), _('February'), _('March'), _('April'), _('May'), _('June'), _('July'), _('August'), _('September'), _('October'), _('November'), _('December')]

    # Serialize data and data_labels to JSON
    data_json = json.dumps(data)
    data_labels_json = json.dumps(data_labels)

    avg_cost_per_liter = 0
    try:
        for refuel in refuels:
            avg_cost_per_liter += refuel.cost / refuel.fuel_amount
            
        avg_cost_per_liter /= len(refuels)
        ## limit to 3 decimal places
        avg_cost_per_liter = round(avg_cost_per_liter, 2)
    except ZeroDivisionError:
        pass

    avg_consumption = 0
    previous_odometer = 0
    try:
        for i, refuel in enumerate(refuels):       
            if i == 0:
                previous_odometer = refuel.odometer
                continue
            avg_consumption += (previous_odometer - refuel.odometer) / refuel.fuel_amount
            previous_odometer = refuel.odometer
        avg_consumption /= len(refuels)
        ## limit to 3 decimal places
        avg_consumption = round(avg_consumption, 2)
    except ZeroDivisionError:
        pass

    try:
        driven_distance = refuels[0].odometer - refuels[len(refuels)-1].odometer
    except IndexError:
        driven_distance = 0

    

    # Prepare the context with vehicle and refuels data
    context = {
        'vehicle': vehicle,
        'refuels': refuels,
        'data_json': data_json,
        'chart_title': chart_title,
        'data_labels_json': data_labels_json,
        'cost_per_liter': avg_cost_per_liter,
        'driven_distance': driven_distance,
        'avg_consumption': avg_consumption,
        'form': form,
        'user_vehicles': user_vehicles,
        'last_refuel': last_refuel,
    }

    # Render the 'vehicle_details.html' template with the context data
    return render(request, 'vehicle_details.html', context=context)


@login_required()
def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)

        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            messages.success(request, _('Vehicle added successfully'))
            return redirect('refuel:vehicle_details', vehicle_id=vehicle.id)
        else:
            messages.error(request, _('Invalid vehicle form'))
            messages.error(request, form.errors)

    else:
        form = VehicleForm()

    fuel_types = FuelType.objects.all()
    context = {
        'form': form,
        'fuel_types': fuel_types,
    }
    return render(request, 'create_vehicle.html', context=context)


@login_required
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.delete()
    messages.success(request, _('Vehicle deleted successfully'))
    return redirect('refuel:user_profile', user_id=request.user.id)