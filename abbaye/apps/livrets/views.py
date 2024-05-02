""" apps/livrets/views.py """

import datetime

from django.http import JsonResponse
from django.shortcuts import render

from modules.dates import date_to_french_string


def home(request):
    """ Home page of Livrets. """
    return render(
        request,
        'livrets/home.html',
        {
            'lines': range(5),
        },
    )


def get_dates(request, *args, **kwargs):
    """ Return a list of 5 dates, according to the start date passed in parameter. """
    items = kwargs['start_date'].split('-')
    start_date = datetime.date(int(items[0]), int(items[1]), int(items[2]))
    dates = [
        date_to_french_string(
            start_date + datetime.timedelta(days=i)
        )
        for i in range(5)
    ]

    return JsonResponse(
        dates,
        safe=False,
    )
