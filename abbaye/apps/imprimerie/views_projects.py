""" apps/imprimerie/views_projects.py """

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .models import Project
from .forms import ProjectForm


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
            return HttpResponseRedirect(reverse('imprimerie:projects_details', args=[project.pk]))

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
    return render(
        request,
        'imprimerie/projects/details.html',
        {
            'project': project,
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
            return HttpResponseRedirect(reverse('imprimerie:projects_details', args=[project.pk]))

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
