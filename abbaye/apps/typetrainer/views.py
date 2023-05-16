""" apps/typetrainer/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Typetrainer. """
    return render(
        request,
        'typetrainer/home.html',
        {},
    )
