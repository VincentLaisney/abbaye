""" apps/livrets/views.py """

from django import forms
from django.shortcuts import render

from .forms import LivretForm, LineForm


def home(request):
    """ Home page of Livrets. """
    Lines = forms.formset_factory(LineForm, extra=5)

    if request.method == 'POST':
        form = LivretForm(request.POST)
        lines = Lines(request.POST)

        if form.is_valid() and lines.is_valid():
            print(form.cleaned_data)
            print(lines.cleaned_data)

    else:
        form = LivretForm()
        lines = Lines()

    return render(
        request,
        'livrets/home.html',
        {
            'form': form,
            'lines': lines,
        }
    )
