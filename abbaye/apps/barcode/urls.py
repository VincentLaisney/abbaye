""" apps/barcode/urls.py """

from django.urls import path

from . import views

app_name = 'barcode'
urlpatterns = [
    path('', views.home, name='home'),
    path(
        'create_barcode/<str:barcode>/',
        views.create_barcode,
        name='create_barcode'
    ),
    path(
        'create_qrcode/<path:qrcode>/',
        views.create_qrcode,
        name='create_qrcode'
    ),
]
