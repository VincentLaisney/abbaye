""" apps/agenda/views.py """

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.main.decorators import group_required
from .forms import EventForm
from .models import Event


def home(request):
    """ Home page of Agenda. """
    events = Event.objects.all().order_by('-date_from', '-date_to')
    return render(
        request,
        'agenda/home.html',
        {'events': events},
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
    """ Details of an agenda. """
    pass


def update(request, **kwargs):
    """ Update an agenda. """
    pass


def delete(request, **kwargs):
    """ Delete an agenda. """
    pass
