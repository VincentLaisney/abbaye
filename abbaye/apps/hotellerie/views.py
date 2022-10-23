""" apps/hotellerie/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Hotellerie. """
    return render(
        request,
        'hotellerie/home.html',
        {},
    )


def list(request):
    """ List of hotelleries. """
    pass


def create(request):
    """ Create an hotellerie. """
    pass


def details(request, **kwargs):
    """ Details of an hotellerie. """
    pass


def update(request, **kwargs):
    """ Update an hotellerie. """
    pass


def delete(request, **kwargs):
    """ Delete an hotellerie. """
    pass
