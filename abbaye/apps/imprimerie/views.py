""" apps/imprimerie/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Imprimerie. """
    return render(
        request, 'imprimerie/home.html', {},
    )


def memo(request):
    """ Memo page imprimerie"""
    return render(
        request, 'imprimerie/memo.html', {},
    )
