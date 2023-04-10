""" apps/agenda/views.py """

from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required
from apps.absences.models import Ticket
from apps.moines.models import Monk
from .forms import EventForm
from .models import Event


def list(request):
    """ List of events. """
    advanced_user = check_advanced_user(request)
    today = date.today()
    days = {}

    for i in range(15):
        day = today + timedelta(i)

        # Events of this day:
        events = Event.objects.filter(
            date_from__lte=day
        ) & Event.objects.filter(
            date_to__gte=day
        ).order_by('category')

        # Feasts of this day:
        feasts = Monk.objects.filter(
            feast_month=day.month
        ) & Monk.objects.filter(
            feast_day=day.day
        ).order_by('absolute_rank', 'entry', 'rank')

        # Absences of this day:
        # TODO.

        days[day] = {
            'date': day,
            'events': events,
            'feasts': feasts,
        }

    return render(
        request,
        'agenda/list.html',
        {
            'advanced_user': advanced_user,
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
            return HttpResponseRedirect(reverse('agenda:list'))

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
        return HttpResponseRedirect(reverse('agenda:list'))

    form = EventForm(instance=event)

    return render(request, 'agenda/delete.html', {
        'form': form,
        'event': event,
    })


def check_advanced_user(request):
    """ Check if a user is advanced, i.e. is in group 'Agenda'
    and thus can access advanced options (create an event, modifying it, etc.). """
    advanced_user = False
    if request.user.is_authenticated:
        if bool(request.user.groups.filter(name='Agenda')) or request.user.is_superuser:
            advanced_user = True
    return advanced_user
