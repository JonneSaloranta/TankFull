
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
]