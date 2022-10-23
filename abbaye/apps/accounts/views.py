""" apps/accounts/views.py """

from django.contrib.auth.views import LoginView

from .forms import AbbayeLoginForm


class AbbayeLoginView(LoginView):
    """ Login view. """
    form_class = AbbayeLoginForm
    template_name = 'accounts/login.html'
