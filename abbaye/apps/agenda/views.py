""" apps/agenda/views.py """

from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required
from .forms import EventForm
from .models import Event


def home(request):
    """ Home page of Agenda. """
    today = date.today()
    days = {}
    for i in range(15):
        day = today + timedelta(i)
        events = Event.objects.filter(
            date_from__lte=day
        ) & Event.objects.filter(
            date_to__gte=day
        )
        days[day] = {
            'events': list(events),
        }
    return render(
        request,
        'agenda/home.html',
        {
            'days': days,
        },
    )


@group_required('Agenda')
def create(request):
    """ Create an event. """
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('agenda:home'))

    form = EventForm()

    return render(request, 'agenda/form.html', {'form': form})


def details(request, **kwargs):
    """ Details of an event. """
    event = get_object_or_404(Event, id=kwargs['pk'])

    return render(
        request,
        'agenda/details.html',
        {
            'event': event,
        }
    )


@group_required('Agenda')
def update(request, **kwargs):
    """ Update an event. """
    event = get_object_or_404(Event, pk=kwargs['pk'])

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'agenda:details',
                    kwargs={
                        'pk': event.pk,
                    }
                )
            )

    form = EventForm(instance=event)

    return render(request, 'agenda/form.html', {
        'form': form,
        'event': event,
    })


@group_required('Agenda')
def delete(request, **kwargs):
    """ Delete an event. """
    event = get_object_or_404(Event, pk=kwargs['pk'])

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        event.delete()
        return HttpResponseRedirect(reverse('agenda:home'))

    form = EventForm(instance=event)

    return render(request, 'agenda/delete.html', {
        'form': form,
        'event': event,
    })
