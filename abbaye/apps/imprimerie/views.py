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
