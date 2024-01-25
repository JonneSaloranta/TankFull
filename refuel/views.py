from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

import os
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection
from django.views.decorators.cache import cache_page

from decouple import config


stats = [
    {
        'name': 'Average consumption',
        'value': '6.5',
    },
    {
        'name': 'Fuel consumed',
        'value': '1000',
    },
    {
        'name': 'Total distance',
        'value': '1000',
    },
    {
        'name': 'Total cost',
        'value': '1000',
    },
]
    

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
    ]

# @cache_page(60 * 15)
def index(request):
    context = {
        'features': features_list,
        'stats': stats
    }

    return render(request, 'index.html' , context=context)

def features(request):
    context = {
        'features': features_list
    }

    return render(request, 'features.html', context=context)

from email_login.models import User
from .models import Vehicle, Refuel

@login_required()
def user_profile(request, user_id):
    user = User.objects.filter(id=user_id).first()
    vehicles = Vehicle.objects.filter(user=user)
    refuels = Refuel.objects.all().order_by('-id')

    context = {
        'user': user,
        'vehicles': vehicles,
        'refuels': refuels,
    }

    return render(request, 'user_profile.html', context=context)