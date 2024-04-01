""" apps/hotellerie/view_parloirs.py """


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse

from apps.main.decorators import group_required

from .forms import ParloirForm
from .models import Parloir


@group_required('Hôtellerie')
def list(request):
    """ List of Parloirs. """
    parloirs = Parloir.objects.all().order_by('-date')
    return render(request, 'hotellerie/parloirs/list.html', {'parloirs': parloirs})


@group_required('Hôtellerie')
def create(request):
    """ Create a Parloir. """
    if request.method == 'POST':
        form = ParloirForm(request.POST)

        if form.is_valid():
            form.save()
            date = form.cleaned_data['date']
            return HttpResponseRedirect(reverse('hotellerie:main_calendar', kwargs={
                'day': '{:%d}'.format(date),
                'month': '{:%m}'.format(date),
                'year': '{:%Y}'.format(date),
            }))

    form = ParloirForm()

    return render(request, 'hotellerie/parloirs/form.html', {'form': form})


@group_required('Hôtellerie')
def details(request, *args, **kwargs):
    """ Details of a Parloir. """
    parloir = get_object_or_404(Parloir, id=kwargs['pk'])

    return render(request, 'hotellerie/parloirs/details.html', {
        'parloir': parloir,
        'calendar_day': parloir.date.strftime('%d'),
        'calendar_month': parloir.date.strftime('%m'),
        'calendar_year': parloir.date.strftime('%Y')
    })


@group_required('Hôtellerie')
def update(request, *args, **kwargs):
    """ Update a Parloir. """
    parloir = get_object_or_404(Parloir, pk=kwargs['pk'])

    if request.method == 'POST':
        form = ParloirForm(request.POST, instance=parloir)
        if form.is_valid():
            form.save()
            date = form.cleaned_data['date']
            return HttpResponseRedirect(reverse('hotellerie:main_calendar', kwargs={
                'day': '{:%d}'.format(date),
                'month': '{:%m}'.format(date),
                'year': '{:%Y}'.format(date),
            }))

    form = ParloirForm(instance=parloir)

    return render(request, 'hotellerie/parloirs/form.html', {
        'form': form,
        'parloir': parloir,
    })


@group_required('Hôtellerie')
def delete(request, *args, **kwargs):
    """ Delete a Parloir. """
    parloir = get_object_or_404(Parloir, pk=kwargs['pk'])

    if request.method == 'POST':
        form = ParloirForm(request.POST, instance=parloir)
        parloir.delete()
        return HttpResponseRedirect(reverse('hotellerie:main_calendar'))

    form = ParloirForm(instance=parloir)

    return render(request, 'hotellerie/parloirs/delete.html', {
        'form': form,
        'parloir': parloir,
    })
