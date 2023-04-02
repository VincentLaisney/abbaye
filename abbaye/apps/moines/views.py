""" apps/moines/views.py """

from datetime import date
from statistics import mean
import os
import numpy
from matplotlib import pyplot

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .forms import MonkForm
from .models import Monk


def home(request):
    """ Home page of monks. """
    return render(
        request,
        'moines/home.html',
        {},
    )


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


@group_required('Moines')
def create(request):
    """ Create a monk. """
    advanced_user = check_advanced_user(request)
    if request.method == 'POST':
        form = MonkForm(request.POST)

        if form.is_valid():
            monk = form.save()
            return HttpResponseRedirect(reverse('moines:details', args=[monk.pk]))

    else:
        form = MonkForm()

    return render(
        request,
        'moines/form.html',
        {
            'form': form,
            'advanced_user': advanced_user,
        }
    )


def details(request, **kwargs):
    """ Details of a monk. """
    monk = get_object_or_404(Monk, pk=kwargs['pk'])
    advanced_user = check_advanced_user(request)
    return render(
        request,
        'moines/details.html',
        {
            'monk': monk,
            'advanced_user': advanced_user,
        }
    )


def update(request, **kwargs):
    """ Update a monk. """
    advanced_user = check_advanced_user(request)
    monk = get_object_or_404(Monk, pk=kwargs['pk'])

    if request.method == 'POST':
        form = MonkForm(request.POST, instance=monk)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('moines:details', args=[monk.pk]))

    else:
        form = MonkForm(instance=monk)

    return render(
        request,
        'moines/form.html',
        {
            'form': form,
            'monk': monk,
            'advanced_user': advanced_user,
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
    monks = len(
        Monk.objects.all()
    )
    postulants = len(
        Monk.objects
        .filter(habit__isnull=True)
    )
    novices = len(
        Monk.objects
        .filter(habit__isnull=False)
        .filter(profession_temp__isnull=True)
    )
    tempo = len(
        Monk.objects
        .filter(profession_temp__isnull=False)
        .filter(profession_perp__isnull=True)
    )
    perpetual = len(
        Monk.objects
        .filter(profession_perp__isnull=False)
    )
    priests = len(
        Monk.objects
        .filter(priest__isnull=False)
    )

    # Average age
    ages = []
    moines = Monk.objects.all()
    for index, moine in enumerate(moines):
        ages.append((date.today() - moine.birthday).days / 365)

    # Histogram:
    hist, bin_edges = numpy.histogram(
        ages,
        bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
    pyplot.figure(figsize=[10, 5])
    result = pyplot.bar(
        [i + 5 for i in bin_edges[:-1]],
        hist,
        width=9,
        color='orange',
    )
    for i, patch in enumerate(result):
        if hist[i] > 0:
            pyplot.text(
                bin_edges[i] + 5, hist[i] + 1, hist[i],
                ha='center',
                va='bottom',
            )
    pyplot.xlim(min(bin_edges), max(bin_edges))
    pyplot.xlabel('Âge', fontsize=10)
    pyplot.ylabel('Nombre de moines', fontsize=10)
    pyplot.xticks(
        numpy.arange(
            min(bin_edges),
            max(bin_edges),
            10
        ),
        fontsize=10
    )
    pyplot.yticks(
        numpy.arange(
            0,
            max(hist) + 15,
            5
        ),
        fontsize=10
    )
    average_age = mean(ages)
    pyplot.text(
        20,
        max(hist) - 5,
        'Moyenne : {:.2f} ans'.format(average_age),
        fontsize=10
    )
    pyplot.savefig(
        os.path.join(settings.MEDIA_ROOT, 'moines/histogram.svg'),
    )

    return render(
        request,
        'moines/statistiques.html',
        {
            'monks': monks,
            'postulants': postulants,
            'novices': novices,
            'tempo': tempo,
            'perpetual': perpetual,
            'priests': priests,
        },
    )


def check_advanced_user(request):
    """ Check if a user is advanced, i.e. is in group 'Moines'
    and thus can modify reserved fields in form ('is_active' etc.). """
    advanced_user = False
    if request.user.is_authenticated:
        if bool(request.user.groups.filter(name='Moines')) or request.user.is_superuser:
            advanced_user = True
    return advanced_user
