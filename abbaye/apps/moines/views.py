""" apps/moines/views.py """

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import MonkForm
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
    if request.method == 'POST':
        form = MonkForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('moines:list'))

    else:
        form = MonkForm()

    return render(request, 'moines/form.html', {'form': form})


def details(request, **kwargs):
    """ Details of a monk. """
    monk = get_object_or_404(Monk, pk=kwargs['pk'])
    return render(
        request,
        'moines/details.html',
        {
            'monk': monk,
        }
    )


def update(request, **kwargs):
    """ Update a monk. """
    monk = get_object_or_404(Monk, pk=kwargs['pk'])

    if request.method == 'POST':
        form = MonkForm(request.POST, instance=monk)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('moines:list'))

    form = MonkForm(instance=monk)

    return render(
        request,
        'moines/form.html',
        {
            'form': form,
            'monk': monk,
        }
    )


def delete(request, **kwargs):
    """ Delete a monk. """
    return render(
        request,
        'moines/delete.html',
        {}
    )


def statistiques(request):
    """ Statistiques view of Monks. """
    return render(
        request,
        'moines/statistiques.html',
        {},
    )
