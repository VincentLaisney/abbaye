""" apps/accenteur/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Accenteur. """
    return render(
        request,
        'accenteur/home.html',
        {},
    )
