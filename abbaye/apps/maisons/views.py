""" apps/maisons/views.py """

from django.shortcuts import render
from django.conf import settings


def home(request):
    """ Home page of Maisons. """
    return render(
        request,
        'maisons/home.html',
        {
            'google_maisons': settings.GOOGLE_MAISONS,
        },
    )
