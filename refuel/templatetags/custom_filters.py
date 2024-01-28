from django import template
from refuel.models import Refuel

register = template.Library()

@register.filter(name='format_decimal')
def format_decimal(value):
    return format(value, '.2f').replace(',', '.')

@register.filter(name='total_distance_traveled')
def total_distance_traveled(value):
    try:
        refuels = Refuel.objects.all()
        return refuels[0].odometer - refuels[len(refuels)-1].odometer
    except IndexError:
        return 0