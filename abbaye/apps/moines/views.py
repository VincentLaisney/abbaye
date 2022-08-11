""" apps/moines/views.py """
from django.shortcuts import render


def home(request):
    """ Home page of Moines. """
    return render(
        request,
        'moines/home.html',
        {},
    )


def list(request):
    """ List of moines. """
    pass


def create(request):
    """ Create a moine. """
    pass


def details(request, **kwargs):
    """ Details of a moine. """
    pass


def update(request, **kwargs):
    """ Update a moine. """
    pass


def delete(request, **kwargs):
    """ Delete a moine. """
    pass
