""" apps/courses/views.py """

from django.shortcuts import render
from django.conf import settings


def home(request):
    """ Home page of Courses. """
    return render(
        request,
        'courses/home.html',
        {
            'google_courses': settings.GOOGLE_COURSES,
        },
    )
