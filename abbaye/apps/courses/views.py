""" apps/courses/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Courses. """
    return render(
        request,
        'courses/home.html',
        {},
    )
