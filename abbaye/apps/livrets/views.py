""" apps/livrets/views.py """
from django.shortcuts import render


def home(request):
    """ Home page of Livrets. """
    return render(
        request,
        'livrets/home.html',
        {},
    )
