""" apps/polyglotte/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Polyglotte. """
    return render(
        request,
        'polyglotte/home.html',
        {},
    )


def list(request):
    """ List of polyglottes. """
    pass


def create(request):
    """ Create a polyglotte. """
    pass


def details(request, **kwargs):
    """ Details of a polyglotte. """
    pass


def update(request, **kwargs):
    """ Update a polyglotte. """
    pass


def delete(request, **kwargs):
    """ Delete a polyglotte. """
    pass
