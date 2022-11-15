""" apps/moines/views.py """
from django.shortcuts import render

from .models import Monk


def home(request):
    """ Home page of Moines. """
    monks = Monk.objects.all().order_by('entry', 'rank')
    return render(
        request,
        'moines/home.html',
        {
            'monks': monks,
        },
    )


def list(request):
    """ List of moines. """
    # TODO
    pass


def create(request):
    """ Create a moine. """
    # TODO
    pass


def details(request, **kwargs):
    """ Details of a moine. """
    # TODO
    pass


def update(request, **kwargs):
    """ Update a moine. """
    # TODO
    pass


def delete(request, **kwargs):
    """ Delete a moine. """
    # TODO
    pass
