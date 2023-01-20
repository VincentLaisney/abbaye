""" apps/imprimerie/views.py """

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Memo
from .forms import MemoForm


def home(request):
    """ Home page of Imprimerie. """
    return render(
        request, 'imprimerie/home.html', {},
    )


def memo(request):
    """ Memo page imprimerie. """
    content = Memo.objects.first().content
    return render(
        request,
        'imprimerie/memo.html',
        {
            'content': content,
        },
    )


def memo_update(request):
    """ Update Memo imprimerie. """
    content = Memo.objects.first()
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=content)
        if form.is_valid():
            content.save()
            return HttpResponseRedirect(
                reverse(
                    'imprimerie:memo',
                )
            )

    else:
        form = MemoForm(instance=content)

    return render(
        request,
        'imprimerie/memo_form.html',
        {
            'form': form,
            'content': content,
        }
    )


def clients_list(request):
    """ List of clients. """


def client_create(request):
    """ Create a client. """


def client_details(request):
    """ Details of client. """


def client_update(request):
    """ Update a client. """


def client_delete(request):
    """ Delete a client. """


def papers_list(request):
    """ List of papers. """


def paper_create(request):
    """ Create a paper. """


def paper_details(request):
    """ Details of a paper. """


def paper_update(request):
    """ Update a paper. """


def paper_delete(request):
    """ Delete a paper. """


def jobs_list(request):
    """ List of jobs. """


def job_create(request):
    """ Create a job. """


def job_details(request):
    """ Details of a job. """


def job_update(request):
    """ Update a job. """


def job_delete(request):
    """ Delete a job. """


def elements_list(request):
    """ List of elements. """


def element_create(request):
    """ Create an element. """


def element_details(request):
    """ Details of an element. """


def element_update(request):
    """ Update an element. """


def element_delete(request):
    """ Delete an element. """
