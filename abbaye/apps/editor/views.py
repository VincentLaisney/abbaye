""" apps/editor/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Editor. """
    return render(
        request,
        'editor/home.html',
        {},
    )


def list(request):
    """ List of editors. """
    pass


def create(request):
    """ Create an editor. """
    pass


def details(request, **kwargs):
    """ Details of an editor. """
    pass


def update(request, **kwargs):
    """ Update an editor. """
    pass


def delete(request, **kwargs):
    """ Delete an editor. """
    pass
