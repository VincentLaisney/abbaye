""" apps/imprimerie/views_papers.py """

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .models import Paper
from .forms import PaperForm


@group_required('Imprimerie')
def list(request):
    """ List of papers. """
    papers = Paper.objects.all().order_by('name', 'weight', 'dim1', 'dim2')
    return render(
        request,
        'imprimerie/papers/list.html',
        {
            'papers': papers,
        }
    )


@group_required('Imprimerie')
def create(request):
    """ Create a paper. """
    if request.method == 'POST':
        form = PaperForm(request.POST)

        if form.is_valid():
            paper = form.save()
            return HttpResponseRedirect(reverse('imprimerie:papers_details', args=[paper.pk]))

    else:
        form = PaperForm()

    return render(
        request,
        'imprimerie/papers/form.html',
        {
            'form': form,
        }
    )


@group_required('Imprimerie')
def details(request, **kwargs):
    """ Details of paper. """
    paper = get_object_or_404(Paper, pk=kwargs['pk'])
    return render(
        request,
        'imprimerie/papers/details.html',
        {
            'paper': paper,
        }
    )


@group_required('Imprimerie')
def update(request, **kwargs):
    """ Update a paper. """
    paper = get_object_or_404(Paper, pk=kwargs['pk'])

    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('imprimerie:papers_details', args=[paper.pk]))

    else:
        form = PaperForm(instance=paper)

    return render(
        request,
        'imprimerie/papers/form.html',
        {
            'form': form,
            'paper': paper,
        }
    )


@group_required('Imprimerie')
def delete(request, **kwargs):
    """ Delete a paper. """
    paper = get_object_or_404(Paper, pk=kwargs['pk'])

    return render(
        request,
        'imprimerie/papers/delete.html',
        {
            'paper': paper,
        }
    )
