""" apps/memo/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Memo. """
    return render(
        request,
        'memo/home.html',
        {},
    )
