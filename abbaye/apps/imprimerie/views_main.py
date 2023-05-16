""" apps/imprimerie/views_main.py """

from django.shortcuts import render


def home(request):
    """ Home page of Imprimerie. """
    return render(
        request, 'imprimerie/main/home.html', {},
    )
