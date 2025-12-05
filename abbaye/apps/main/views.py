""" apps/main/views.py """

from django.shortcuts import render
from django.conf import settings


def home(request):
    """ Home page of main. """
    return render(
        request,
        'main/home.html',
        {
            'google_services': settings.GOOGLE_SERVICES,
        },
    )
