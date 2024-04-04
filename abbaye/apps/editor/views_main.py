""" apps/editor/views_main.py """

from django.shortcuts import render


def home(request):
    """ Home view of Editor. """
    return render(request, 'editor/home.html')
