""" apps/hotellerie/view_retraites.py """


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .forms import RetreatForm
from .models import Retreat


@group_required('Hôtellerie')
def list(request):
    """ List of retreats. """
    retreats = Retreat.objects.all().order_by('-date_from')
    return render(
        request,
        'hotellerie/retreats/list.html',
        {
            'retreats': retreats,
        }
    )


@group_required('Hôtellerie')
def create(request):
    """ Create a Retreat. """
    if request.method == 'POST':
        form = RetreatForm(request.POST)

        if form.is_valid():
            form.save()
            date = form.cleaned_data['date_from']
            return HttpResponseRedirect(reverse('hotellerie:main_calendar', kwargs={
                'day': '{:%d}'.format(date),
                'month': '{:%m}'.format(date),
                'year': '{:%Y}'.format(date),
            }))

    form = RetreatForm()

    return render(request, 'hotellerie/retreats/form.html', {'form': form})


@group_required('Hôtellerie')
def details(request, *args, **kwargs):
    """ Details of a Retreat. """
    retreat = get_object_or_404(Retreat, pk=kwargs['pk'])
    return render(request, 'hotellerie/retreats/details.html', {
        'retreat': retreat
    })


@group_required('Hôtellerie')
def update(request, **kwargs):
    """ Update a Retreat. """
    retreat = get_object_or_404(Retreat, pk=kwargs['pk'])

    if request.method == 'POST':
        form = RetreatForm(request.POST, instance=retreat)

        if form.is_valid():
            form.save()
            date = form.cleaned_data['date_from']
            return HttpResponseRedirect(reverse('hotellerie:main_calendar', kwargs={
                'day': '{:%d}'.format(date),
                'month': '{:%m}'.format(date),
                'year': '{:%Y}'.format(date),
            }))

    form = RetreatForm(instance=retreat)

    return render(request, 'hotellerie/retreats/form.html', {
        'form': form,
        'retreat': retreat,
    })


@group_required('Hôtellerie')
def delete(request, **kwargs):
    """ Delete a Retreat. """
    retreat = get_object_or_404(Retreat, pk=kwargs['pk'])

    if request.method == 'POST':
        form = RetreatForm(request.POST, instance=retreat)
        retreat.delete()
        return HttpResponseRedirect(reverse('hotellerie:main_calendar'))

    form = RetreatForm(instance=retreat)

    return render(request, 'hotellerie/retreats/delete.html', {
        'form': form,
        'retreat': retreat,
    })
