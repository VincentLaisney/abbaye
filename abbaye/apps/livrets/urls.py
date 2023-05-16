""" apps/livrets/urls.py """

from django.urls import path

from . import views

app_name = 'livrets'
urlpatterns = [
    path('', views.home, name='home'),
]
