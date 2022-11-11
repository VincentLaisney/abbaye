""" apps/agenda/views.py """

from django.shortcuts import render

from .models import Item


def home(request):
    """ Home page of Ornitho. """
    return render(
        request,
        'ornitho/home.html',
        {},
    )


def list(request, **kwargs):
    """ List of items. """
    items = Item.objects.all().order_by('name')
    if kwargs:
        category = kwargs['category']
        category_uppercase = {
            'oiseaux': 'Oiseaux',
            'mammiferes': 'Mammifères',
            'reptiles': 'Reptiles',
            'amphibiens': 'Amphibiens',
            'libellules': 'Libellules',
            'papillons': 'Papillons',
            'sauterelles': 'Sauterelles',
        }[category]
        column_sound = category in [
            'oiseaux',
            'mammiferes',
            'amphibiens',
            'sauterelles',
        ]
        items = Item.objects.filter(category=category).order_by('name')
    else:
        category_uppercase = ''
        column_sound = True
        items = Item.objects.all().order_by('name')
    return render(
        request,
        'ornitho/list.html',
        {
            'items': items,
            'category_uppercase': category_uppercase,
            'column_sound': column_sound,
        }
    )


def galleria(request):
    """ Galleria of pictures. """
    return render(
        request,
        'ornitho/galleria.html',
        {},
    )
