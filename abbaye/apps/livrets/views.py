""" apps/livrets/views.py """

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    """ Home page of Livrets. """
    return render(
        request,
        'livrets/home.html',
        {},
    )


def pdf(request, *args, **kwargs):
    """ Return OK when PDF is created. """
    data = request.GET
    return JsonResponse(
        {'back': 'OK'},
    )
