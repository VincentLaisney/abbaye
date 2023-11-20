""" apps/imprimerie/forms.py """

from django import forms

from .models import Memo


class MemoForm(forms.ModelForm):
    """ Form for Memo. """
    class Meta:
        model = Memo
        fields = [
            'content',
        ]
