""" apps/moines/views.py """
from django.shortcuts import render

from .models import Monk


def list(request):
    """ List of monks. """
    monks = Monk.objects.all().order_by('entry', 'rank')
    return render(
        request,
        'moines/list.html',
        {
            'monks': monks,
        },
    )


def create(request):
    """ Create a monk. """
    # TODO
    pass


def details(request, **kwargs):
    """ Details of a monk. """
    return render(
        request,
        'moines/details.html',
        {}
    )


def update(request, **kwargs):
    """ Update a monk. """
    # TODO
    pass


def delete(request, **kwargs):
    """ Delete a monk. """


def statistiques(request):
    """ Statistiques view of Monks. """
    return render(
        request,
        'moines/statistiques.html',
        {},
    )
