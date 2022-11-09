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
        items = Item.objects.filter(category=category).order_by('name')
    else:
        items = Item.objects.all().order_by('name')
    return render(
        request,
        'ornitho/list.html',
        {
            'items': items,
            'category_uppercase': category_uppercase if category_uppercase else '',
        }
    )


def galleria(request):
    """ Galleria of pictures. """
    return render(
        request,
        'ornitho/galleria.html',
        {},
    )
