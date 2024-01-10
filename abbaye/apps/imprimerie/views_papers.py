""" apps/imprimerie/views_papers.py """

from dal import autocomplete

from django.core.serializers import serialize
from django.http import HttpResponseRedirect, JsonResponse
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
            return HttpResponseRedirect(reverse('imprimerie:paper_details', args=[paper.pk]))

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
            return HttpResponseRedirect(reverse('imprimerie:paper_details', args=[paper.pk]))

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


class PaperAutocompleteView(autocomplete.Select2QuerySetView):
    """ Return a set of Papers according to the user search value. """

    def get_queryset(self):
        papers = Paper.objects.filter(
            name__icontains=self.q
        ) | Paper.objects.filter(
            weight__icontains=self.q
        ) | Paper.objects.filter(
            dim1__icontains=self.q
        ) | Paper.objects.filter(
            dim2__icontains=self.q
        )
        return papers .order_by('name')


def fetch_paper_data(request, **kwargs):
    """ Returns the data of a Paper as an array, for Ajax. """
    paper = serialize(
        'json',
        Paper.objects.filter(pk=kwargs['id_paper'])
    )
    return JsonResponse(paper, safe=False)
