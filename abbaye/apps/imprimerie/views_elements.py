""" apps/imprimerie/views_elements.py """

from django.shortcuts import render

from apps.main.decorators import group_required

from .models import Element


@group_required('Imprimerie')
def list(request):
    """ List of elements. """
    return render(
        request,
        'imprimerie/elements/list.html',
        {}
    )


@group_required('Imprimerie')
def create(request):
    """ Create a paper. """
    return render(
        request,
        'imprimerie/elements/form.html',
        {}
    )


@group_required('Imprimerie')
def details(request):
    """ Details of paper. """
    return render(
        request,
        'imprimerie/elements/details.html',
        {}
    )


@group_required('Imprimerie')
def update(request):
    """ Update a paper. """
    return render(
        request,
        'imprimerie/elements/form.html',
        {}
    )


@group_required('Imprimerie')
def delete(request):
    """ Delete a paper. """
    return render(
        request,
        'imprimerie/elements/delete.html',
        {}
    )
