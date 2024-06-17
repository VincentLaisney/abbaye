""" apps/ordomatic/urls.py """

from django.urls import path

from . import views

app_name = 'ordomatic'
urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.home_new, name='home_new'),
]
