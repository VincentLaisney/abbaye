""" apps/typetrainer/urls.py """

from django.urls import path

from . import views

app_name = 'typetrainer'
urlpatterns = [
    path('', views.home, name='home'),
]
