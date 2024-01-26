
from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    path('charts/', views.charts, name='charts'),
    ## API
    path('user/<int:user_id>/vehicles/', views.user_vehicles, name='user_vehicles'),
    path('user/<int:user_id>/details/', views.user_details, name='user_details'),
    path('vehicle/<int:vehicle_id>/details/', views.vehicle_details, name='vehicle_details'),
    path('refuel/<int:refuel_id>/details/', views.refuel_details, name='refuel_details'),
    path('vehicle/<int:vehicle_id>/refuels/', views.vehicle_refuels, name='vehicle_refuels'),
    path('user/<int:user_id>/refuels/', views.user_refuels, name='user_refuels'),
    path('vehicle/<int:vehicle_id>/update/', views.update_vehicle, name='update_vehicle'),
    path('vehicle/create/', views.create_vehicle, name='create_vehicle'),
    path('fuel_types/', views.get_fuel_types, name='get_fuel_types'),
]