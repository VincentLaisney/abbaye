""" apps/imprimerie/views_work.py """


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Work
from .forms import WorkForm


def work(request):
    """ Work imprimerie. """
    quill = Work.objects.first()
    return render(
        request,
        'imprimerie/work/work.html',
        {
            'quill': quill,
        },
    )


def work_update(request):
    """ Update Work imprimerie. """
    content = Work.objects.first()
    if request.method == 'POST':
        form = WorkForm(request.POST, instance=content)
        if form.is_valid():
            content.save()
            return HttpResponseRedirect(
                reverse(
                    'imprimerie:work',
                )
            )

    else:
        form = WorkForm(instance=content)

    return render(
        request,
        'imprimerie/work/form.html',
        {
            'form': form,
            'content': content,
        }
    )
