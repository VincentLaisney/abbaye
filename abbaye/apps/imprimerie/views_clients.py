""" apps/imprimerie/views_clients.py """

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .models import Client
from .forms import ClientForm


@group_required('Imprimerie')
def list(request):
    """ List of clients. """
    clients = Client.objects.all().order_by('last_name', 'first_name')
    return render(
        request,
        'imprimerie/clients/list.html',
        {
            'clients': clients,
        }
    )


@group_required('Imprimerie')
def create(request):
    """ Create a client. """
    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            client = form.save()
            return HttpResponseRedirect(reverse('imprimerie:clients_details', args=[client.pk]))

    else:
        form = ClientForm()

    return render(
        request,
        'imprimerie/clients/form.html',
        {
            'form': form,
        }
    )


@group_required('Imprimerie')
def details(request, **kwargs):
    """ Details of client. """
    client = get_object_or_404(Client, pk=kwargs['pk'])
    return render(
        request,
        'imprimerie/clients/details.html',
        {
            'client': client,
        }
    )


@group_required('Imprimerie')
def update(request, **kwargs):
    """ Update a client. """
    client = get_object_or_404(Client, pk=kwargs['pk'])

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('imprimerie:clients_details', args=[client.pk]))

    else:
        form = ClientForm(instance=client)

    return render(
        request,
        'imprimerie/clients/form.html',
        {
            'form': form,
            'client': client,
        }
    )


@group_required('Imprimerie')
def delete(request, **kwargs):
    """ Delete a client. """
    client = get_object_or_404(Client, pk=kwargs['pk'])
    return render(
        request,
        'imprimerie/clients/delete.html',
        {
            'client': client,
        }
    )
