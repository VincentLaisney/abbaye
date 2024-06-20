""" apps/ordomatic/views.py """

from datetime import date
from django.shortcuts import render


def home(request):
    """ Home page of Ordomatic. """
    year = date.today().year
    return render(
        request,
        'ordomatic/home.html',
        {
            'year': year,
        },
    )
