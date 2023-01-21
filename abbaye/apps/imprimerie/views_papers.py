""" apps/imprimerie/views_papers.py """

from django.shortcuts import render

from apps.main.decorators import group_required

from .models import Paper


@group_required('Imprimerie')
def list(request):
    """ List of papers. """
    return render(
        request,
        'imprimerie/papers/list.html',
        {}
    )


@group_required('Imprimerie')
def create(request):
    """ Create a paper. """
    return render(
        request,
        'imprimerie/papers/form.html',
        {}
    )


@group_required('Imprimerie')
def details(request):
    """ Details of paper. """
    return render(
        request,
        'imprimerie/papers/details.html',
        {}
    )


@group_required('Imprimerie')
def update(request):
    """ Update a paper. """
    return render(
        request,
        'imprimerie/papers/form.html',
        {}
    )


@group_required('Imprimerie')
def delete(request):
    """ Delete a paper. """
    return render(
        request,
        'imprimerie/papers/delete.html',
        {}
    )
