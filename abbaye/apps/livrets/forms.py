""" apps/livrets/forms.py """

from django import forms


class LivretForm(forms.Form):
    """ Form for Livret. """
    date = forms.DateField()


class LineForm(forms.Form):
    """ Form for Line. """
    IN = forms.CharField(
        label='IN',
        label_suffix='',
        required=False,
    )
    GR = forms.CharField(
        label='GR',
        label_suffix='',
        required=False,
    )
    AL = forms.CharField(
        label='AL',
        label_suffix='',
        required=False,
    )
    OF = forms.CharField(
        label='OF',
        label_suffix='',
        required=False,
    )
    CO = forms.CharField(
        label='CO',
        label_suffix='',
        required=False,
    )
    KY = forms.CharField(
        label='KY',
        label_suffix='',
        required=False,
    )
    GL = forms.CharField(
        label='GL',
        label_suffix='',
        required=False,
    )
    SA = forms.CharField(
        label='SA',
        label_suffix='',
        required=False,
    )
    CR = forms.CharField(
        label='CR',
        label_suffix='',
        required=False,
    )
