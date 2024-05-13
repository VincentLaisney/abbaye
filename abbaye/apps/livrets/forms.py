""" apps/livrets/forms.py """

from django import forms


class LivretForm(forms.Form):
    """ Form for Livret. """
    date = forms.DateField(
        label='Date de départ',
    )


class LineForm(forms.Form):
    """ Form for Line. """
    IN = forms.CharField(
        label='IN',
        required=False,
    )
    GR = forms.CharField(
        label='GR',
        required=False,
    )
    AL = forms.CharField(
        label='AL',
        required=False,
    )
    OF = forms.CharField(
        label='OF',
        required=False,
    )
    CO = forms.CharField(
        label='CO',
        required=False,
    )
    KY = forms.CharField(
        label='KY',
        required=False,
    )
    GL = forms.CharField(
        label='GL',
        required=False,
    )
    SA = forms.CharField(
        label='SA',
        required=False,
    )
    CR = forms.CharField(
        label='CR',
        required=False,
    )
