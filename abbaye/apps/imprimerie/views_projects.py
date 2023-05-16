""" apps/imprimerie/views_projects.py """

from django.shortcuts import render

from apps.main.decorators import group_required

from .models import Project


@group_required('Imprimerie')
def list(request):
    """ List of projects. """
    return render(
        request,
        'imprimerie/projects/list.html',
        {}
    )


@group_required('Imprimerie')
def create(request):
    """ Create a paper. """
    return render(
        request,
        'imprimerie/projects/form.html',
        {}
    )


@group_required('Imprimerie')
def details(request):
    """ Details of paper. """
    return render(
        request,
        'imprimerie/projects/details.html',
        {}
    )


@group_required('Imprimerie')
def update(request):
    """ Update a paper. """
    return render(
        request,
        'imprimerie/projects/form.html',
        {}
    )


@group_required('Imprimerie')
def delete(request):
    """ Delete a paper. """
    return render(
        request,
        'imprimerie/projects/delete.html',
        {}
    )
