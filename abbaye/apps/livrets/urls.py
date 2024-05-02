""" apps/livrets/urls.py """

from django.urls import path

from . import views

app_name = 'livrets'
urlpatterns = [
    path('', views.home, name='home'),
    path('get_dates/<str:start_date>/', views.get_dates, name='get_dates'),
]
