""" apps/jgabc/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Jgabc. """
    return render(
        request,
        'jgabc/home.html',
        {},
    )
