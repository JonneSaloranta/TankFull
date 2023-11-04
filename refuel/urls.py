
from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
]