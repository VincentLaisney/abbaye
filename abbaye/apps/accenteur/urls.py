""" apps/accenteur/urls.py """

from django.urls import path

from . import views

app_name = 'accenteur'
urlpatterns = [
    path('', views.home, name='home'),
]
