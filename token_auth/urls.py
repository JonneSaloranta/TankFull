from django.urls import re_path
from . import views

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('reset_token', views.reset_token),
    re_path('delete_token', views.delete_token),
]