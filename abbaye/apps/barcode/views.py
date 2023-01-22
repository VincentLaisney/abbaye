""" apps/barcode/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Barcode. """
    return render(
        request,
        'barcode/home.html',
        {},
    )
