""" apps/statistiques/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Statistiques. """
    return render(
        request,
        'statistiques/home.html',
        {},
    )


def list(request):
    """ List of statistiques. """
    pass


def create(request):
    """ Create a statistique. """
    pass


def details(request, **kwargs):
    """ Details of a statistique. """
    pass


def update(request, **kwargs):
    """ Update a statistique. """
    pass


def delete(request, **kwargs):
    """ Delete a statistique. """
    pass
