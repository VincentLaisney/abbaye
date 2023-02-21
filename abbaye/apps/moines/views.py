""" apps/moines/views.py """

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

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
    return render(
        request,
        'moines/details.html',
        {
            'monk': monk,
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
    return render(
        request,
        'moines/statistiques.html',
        {},
    )


def check_advanced_user(request):
    """ Check if a user is advanced, i.e. is in group 'Moines'
    and thus can modify reserved fields in form ('is_active' etc.). """
    advanced_user = False
    if request.user.is_authenticated:
        if bool(request.user.groups.filter(name='Moines')) or request.user.is_superuser:
            advanced_user = True
    return advanced_user
