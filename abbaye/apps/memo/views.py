""" apps/memo/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Memo. """
    return render(
        request,
        'memo/home.html',
        {},
    )


def install(request):
    """ Installation view."""
    return render(
        request,
        'memo/install.html',
        {}
    )


def commands(request):
    """ Commands view."""
    return render(
        request,
        'memo/commands.html',
        {}
    )


def sh(request):
    """ Scripts view."""
    return render(
        request,
        'memo/sh.html',
        {}
    )


def py(request):
    """ Python view."""
    return render(
        request,
        'memo/py.html',
        {}
    )


def js(request):
    """ Javascript view."""
    return render(
        request,
        'memo/js.html',
        {}
    )


def mysql(request):
    """ Mysql view."""
    return render(
        request,
        'memo/mysql.html',
        {}
    )


def vim(request):
    """ Vim view."""
    return render(
        request,
        'memo/vim.html',
        {}
    )


def git(request):
    """ Git view."""
    return render(
        request,
        'memo/git.html',
        {}
    )
