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
from .serializers import VehicleSerializer  # Import the VehicleSerializer

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

from email_login.models import User
from .models import Vehicle, Refuel
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

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

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_vehicles(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    vehicles = Vehicle.objects.filter(user=user)
    serialized_vehicles = VehicleSerializer(vehicles, many=True).data
    return Response({'user': UserSerializer(instance=user).data, 'vehicles': serialized_vehicles}, status=status.HTTP_200_OK)