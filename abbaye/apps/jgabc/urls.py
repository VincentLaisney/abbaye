""" apps/barcode/urls.py """

from django.urls import path

from . import views

app_name = 'jgabc'
urlpatterns = [
    path('', views.home, name='home'),
]
