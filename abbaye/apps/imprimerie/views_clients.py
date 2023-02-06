""" apps/imprimerie/views_clients.py """

from django.shortcuts import render

from apps.main.decorators import group_required

from .models import Client


@group_required('Imprimerie')
def list(request):
    """ List of clients. """
    return render(
        request,
        'imprimerie/clients/list.html',
        {}
    )


@group_required('Imprimerie')
def create(request):
    """ Create a client. """
    return render(
        request,
        'imprimerie/clients/form.html',
        {}
    )


@group_required('Imprimerie')
def details(request):
    """ Details of client. """
    return render(
        request,
        'imprimerie/clients/details.html',
        {}
    )


@group_required('Imprimerie')
def update(request):
    """ Update a client. """
    return render(
        request,
        'imprimerie/clients/form.html',
        {}
    )


@group_required('Imprimerie')
def delete(request):
    """ Delete a client. """
    return render(
        request,
        'imprimerie/clients/delete.html',
        {}
    )
