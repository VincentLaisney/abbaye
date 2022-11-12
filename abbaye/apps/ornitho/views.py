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


def galerie(request):
    """ Galerie home. """
    return render(
        request,
        'ornitho/galerie.html',
        {},
    )


def galerie_paysages(request):
    """ Galerie paysages. """
    return render(
        request,
        'ornitho/galerie-paysages.html',
        {},
    )


def galerie_oiseaux(request):
    """ Galerie oiseaux. """
    return render(
        request,
        'ornitho/galerie-oiseaux.html',
        {},
    )


def galerie_mammiferes(request):
    """ Galerie mammifères. """
    return render(
        request,
        'ornitho/galerie-mammiferes.html',
        {},
    )


def galerie_insectes(request):
    """ Galerie insectes. """
    return render(
        request,
        'ornitho/galerie-insectes.html',
        {},
    )


def galerie_reptiles_amphibiens(request):
    """ Galerie reptiles et amphibiens. """
    return render(
        request,
        'ornitho/galerie-reptiles-amphibiens.html',
        {},
    )


def galerie_plantes(request):
    """ Galerie plantes. """
    return render(
        request,
        'ornitho/galerie-plantes.html',
        {},
    )


def galerie_flavigny(request):
    """ Galerie Flavigny. """
    return render(
        request,
        'ornitho/galerie-flavigny.html',
        {},
    )
