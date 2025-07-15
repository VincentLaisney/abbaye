""" apps/maisons/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Maisons. """
    return render(
        request,
        'maisons/home.html',
        {},
    )
