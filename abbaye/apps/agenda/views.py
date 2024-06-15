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


def agenda_as_list(request, *args, **kwargs):
    """ Agenda as list. """
    advanced_user = check_advanced_user(request)
    if 'date' in kwargs.keys():
        day = date.fromisoformat(kwargs['date'])
    else:
        day = date.today()
    days = fetch_data(day, 30)
    return render(
        request,
        'agenda/list.html',
        {
            'advanced_user': advanced_user,
            'days': days,
            'day_as_string': day.strftime("%d/%m/%Y"),
        },
    )


def agenda_as_calendar(request, *args, **kwargs):
    """ Agenda as calendar. """
    advanced_user = check_advanced_user(request)
    if 'date' in kwargs.keys():
        arg_date = date.fromisoformat(kwargs['date'])
    else:
        arg_date = date.today()
    initial = arg_date - (
        timedelta(
            (arg_date.weekday() + 1) if arg_date.weekday() != 6
            else 0
        )
    )
    data = fetch_data(initial, 7)
    days = {}
    for index, item in enumerate(data):
        day = data[item]['date']
        days[day] = {}
        days[day]['current'] = (item == date.today())
        days[day]['events'] = {}
        days[day]['feasts'] = {}
        days[day]['absences'] = {}
        days[day]['presences'] = {}

        for event in data[item]['events']:
            if event.date_from == item or (index == 0 and event.date_from < item <= event.date_to):
                arrow_left = arrow_right = False
                if index == 0 and event.date_from < item <= event.date_to:
                    length = (event.date_to - initial).days + 1
                    arrow_left = True
                else:
                    length = (event.date_to - event.date_from).days + 1
                if length > (7 - index):
                    length = 7 - index
                    arrow_right = True

                days[day]['events'][event] = {
                    'x': index + 1,
                    'length': length,
                    'event': event,
                    'arrow_left': arrow_left,
                    'arrow_right': arrow_right,
                }

        for feast in data[item]['feasts']:
            days[day]['feasts'][feast] = {
                'x': index + 1,
                'length': 1,
                'feast': feast,
            }

        for absence in data[item]['absences']:
            if absence.go_date == item or (index == 0 and absence.go_date < item <= absence.back_date):
                arrow_left = arrow_right = False
                if index == 0 and absence.go_date < item <= absence.back_date:
                    length = (absence.back_date - initial).days + 1
                    arrow_left = True
                else:
                    length = (absence.back_date - absence.go_date).days + 1
                if length > (7 - index):
                    length = 7 - index
                    arrow_right = True

                days[day]['absences'][absence] = {
                    'x': index + 1,
                    'length': length,
                    'absence': absence,
                    'arrow_left': arrow_left,
                    'arrow_right': arrow_right,
                }

        for presence in data[item]['presences']:
            if presence.go_date == item or (index == 0 and presence.go_date < item <= presence.back_date):
                arrow_left = arrow_right = False
                if index == 0 and presence.go_date < item <= presence.back_date:
                    length = (presence.back_date - initial).days + 1
                    arrow_left = True
                else:
                    length = (presence.back_date - presence.go_date).days + 1
                if length > (7 - index):
                    length = 7 - index
                    arrow_right = True

                days[day]['presences'][presence] = {
                    'x': index + 1,
                    'length': length,
                    'presence': presence,
                    'arrow_left': arrow_left,
                    'arrow_right': arrow_right,
                }

    return render(
        request,
        'agenda/calendar.html',
        {
            'advanced_user': advanced_user,
            'days': days,
            'day_as_string': arg_date.strftime("%d/%m/%Y"),
        },
    )


@group_required('Agenda')
def create(request):
    """ Create an event. """
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('agenda:calendar'))

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
                    'agenda:calendar',
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
        return HttpResponseRedirect(reverse('agenda:calendar'))

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


def fetch_data(initial, length):
    """ Fetch everything from today. """
    days = {}
    for i in range(length):
        day = initial + timedelta(i)

        # Events of this day:
        events = Event.objects.filter(
            date_from__lte=day
        ) & Event.objects.filter(
            date_to__gte=day
        ).order_by('category', 'name')

        # Feasts of this day:
        feasts = Monk.objects.filter(
            feast_month=day.month
        ) & Monk.objects.filter(
            feast_day=day.day
        ).order_by('absolute_rank', 'entry', 'rank_entry')

        # Absences of this day:
        absences = Ticket.objects \
            .filter(
                type='out'
            ) & Ticket.objects.filter(
                go_date__lte=day
            ) & Ticket.objects.filter(
                back_date__gte=day
            ) \
            .order_by('go_date', 'back_date')

        # Presences of this day:
        presences = Ticket.objects \
            .filter(
                type='in'
            ) & Ticket.objects.filter(
                go_date__lte=day
            ) & Ticket.objects.filter(
                back_date__gte=day
            ) \
            .order_by('go_date', 'back_date')

        days[day] = {
            'date': day,
            'events': events,
            'feasts': feasts,
            'absences': absences,
            'presences': presences,
        }

    return days
