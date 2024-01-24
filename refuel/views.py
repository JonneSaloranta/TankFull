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
            'name': 'Keep track',
            'description': 'Keep track of your refuels and see how much you have spent on fuel.',
            'icon': 'bi bi-database'
        },
        {
            'name': 'Statistics',
            'description': 'See your refuel statistics in a graph.',
            'icon': 'bi bi-graph-up'
        },
        {
            'name': 'Compare',
            'description': 'Compare your refuels to others.',
            'icon': 'bi bi-people'
        },
        {
            'name': _('Share'),
            'description': _('Share your refuels with others.'),
            'icon': 'bi bi-share'
        },
        {
            'name': _('Export'),
            'description': _('Export your refuels to a file.'),
            'icon': 'bi bi-file-earmark-arrow-down'
        },
        {
            'name': _('Import'),
            'description': _('Import your refuels from a file.'),
            'icon': 'bi bi-file-earmark-arrow-up'
        },
    ]

@cache_page(60 * 15)
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