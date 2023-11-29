""" apps/imprimerie/views_projects.py """

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .models import Element, Project
from .forms import ElementForm, ProjectForm


@group_required('Imprimerie')
def list(request):
    """ List of projects. """
    projects = Project.objects.all().order_by('-modified')
    return render(
        request,
        'imprimerie/projects/list.html',
        {
            'projects': projects,
        }
    )


@group_required('Imprimerie')
def create(request):
    """ Create a project. """
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save()
            return HttpResponseRedirect(reverse('imprimerie:project_details', args=[project.pk]))

    else:
        form = ProjectForm()

    return render(
        request,
        'imprimerie/projects/form.html',
        {
            'form': form,
        }
    )


@group_required('Imprimerie')
def details(request, **kwargs):
    """ Details of project. """
    project = get_object_or_404(Project, pk=kwargs['pk'])
    elements = Element.objects.filter(project=project)
    return render(
        request,
        'imprimerie/projects/details.html',
        {
            'project': project,
            'elements': elements,
        }
    )


@group_required('Imprimerie')
def update(request, **kwargs):
    """ Update a project. """
    project = get_object_or_404(Project, pk=kwargs['pk'])

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('imprimerie:project_details', args=[project.pk]))

    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        'imprimerie/projects/form.html',
        {
            'form': form,
            'project': project,
        }
    )


@group_required('Imprimerie')
def delete(request, **kwargs):
    """ Delete a project. """
    project = get_object_or_404(Project, pk=kwargs['pk'])
    return render(
        request,
        'imprimerie/projects/delete.html',
        {
            'project': project,
        }
    )


@group_required('Imprimerie')
def create_element(request, **kwargs):
    """ Create an element for a project. """
    project = get_object_or_404(Project, pk=kwargs['pk_project'])
    if request.method == 'POST':
        form = ElementForm(request.POST)

        if form.is_valid():
            element = form.save(commit=False)
            element.project = project
            element.save()
            return HttpResponseRedirect(reverse('imprimerie:projects_details', args=[project.pk]))

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
def update_element(request, **kwargs):
    """ Update an element for a project. """
    element = get_object_or_404(Element, pk=kwargs['pk'])
    project = get_object_or_404(Project, pk=kwargs['pk_project'])

    if request.method == 'POST':
        form = ElementForm(request.POST, instance=element)

        if form.is_valid():
            element = form.save(commit=False)
            element.project = project
            element.save()
            return HttpResponseRedirect(reverse('imprimerie:projects_details', args=[project.pk]))

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
def delete_element(request, **kwargs):
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
