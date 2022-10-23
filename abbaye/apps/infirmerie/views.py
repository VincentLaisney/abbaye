""" apps/infirmerie/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Infirmerie. """
    return render(
        request,
        'infirmerie/home.html',
        {},
    )


def list(request):
    """ List of infirmeries. """
    pass


def create(request):
    """ Create an infirmerie. """
    pass


def details(request, **kwargs):
    """ Details of an infirmerie. """
    pass


def update(request, **kwargs):
    """ Update an infirmerie. """
    pass


def delete(request, **kwargs):
    """ Delete an infirmerie. """
    pass
