from django import template
from refuel.models import Refuel
from django.contrib.auth import get_user_model

register = template.Library()

@register.filter(name='format_decimal')
def format_decimal(value):
    return format(value, '.2f').replace(',', '.')

@register.filter(name='total_distance_traveled')
def total_distance_traveled(value):
    return 0
    

@register.filter(name='number_of_active_users')
def active_users(value):
    return get_user_model().objects.filter(is_active=True).count()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})