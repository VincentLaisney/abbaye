""" apps/imprimerie/views_elements.py """

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .models import Element, Project
from .forms import ElementForm


@group_required('Imprimerie')
def create(request, **kwargs):
    """ Create an element for a project. """
    project = get_object_or_404(Project, pk=kwargs['pk_project'])
    if request.method == 'POST':
        form = ElementForm(request.POST)

        if form.is_valid():
            element = form.save(commit=False)
            element.project = project
            element.save()
            return HttpResponseRedirect(reverse('imprimerie:project_details', args=[project.pk]))

    else:
        form = ElementForm()

    return render(
        request,
        'imprimerie/elements/form.html',
        {
            'form': form,
            'project': project,
        }
    )


@group_required('Imprimerie')
def details(request, **kwargs):
    """ Details of an element. """
    element = get_object_or_404(Element, pk=kwargs['pk'])
    project = get_object_or_404(Project, pk=kwargs['pk_project'])

    return render(
        request,
        'imprimerie/elements/details.html',
        {
            'element': element,
            'project': project,
        }
    )


@group_required('Imprimerie')
def update(request, **kwargs):
    """ Update an element for a project. """
    element = get_object_or_404(Element, pk=kwargs['pk'])
    project = get_object_or_404(Project, pk=kwargs['pk_project'])

    if request.method == 'POST':
        form = ElementForm(request.POST, instance=element)

        if form.is_valid():
            element = form.save(commit=False)
            element.project = project
            element.save()
            return HttpResponseRedirect(reverse('imprimerie:project_details', args=[project.pk]))

    else:
        form = ElementForm(instance=element)

    return render(
        request,
        'imprimerie/elements/form.html',
        {
            'form': form,
            'element': element,
            'project': project,
        }
    )


@group_required('Imprimerie')
def delete(request, **kwargs):
    """ Delete an element for a project. """
    element = get_object_or_404(Element, pk=kwargs['pk'])
    project = get_object_or_404(Project, pk=kwargs['pk_project'])
    return render(
        request,
        'imprimerie/elements/delete.html',
        {
            'project': project,
            'element': element,
        }
    )
