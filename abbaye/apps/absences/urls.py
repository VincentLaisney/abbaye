""" apps/absences/urls.py """

from django.urls import path

from . import views

app_name = 'absences'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/<str:action>/', views.create, name='create'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failure'),
]
