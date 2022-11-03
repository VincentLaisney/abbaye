""" apps/agenda/views.py """

from django.shortcuts import render

from .models import Item


def home(request):
    """ Home page of Ornitho. """
    items = Item.objects.all().order_by('name')
    return render(
        request,
        'ornitho/home.html',
        {
            'items': items,
        },
    )
