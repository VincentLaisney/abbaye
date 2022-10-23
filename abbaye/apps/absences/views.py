""" apps/absences/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Absences. """
    return render(
        request,
        'absences/home.html',
        {},
    )


def list(request):
    """ List of absences. """
    return render(
        request,
        'absences/list.html',
        {},
    )


def create(request):
    """ Create an absence. """
    pass


def details(request, **kwargs):
    """ Details of an absence. """
    pass


def update(request, **kwargs):
    """ Update an absence. """
    pass


def delete(request, **kwargs):
    """ Delete an absence. """
    pass
