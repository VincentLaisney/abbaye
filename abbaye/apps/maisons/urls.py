""" apps/maisons/urls.py """

from django.urls import path

from . import views

app_name = 'maisons'
urlpatterns = [
    path('', views.home, name='home'),
]
