""" apps/imprimerie/forms.py """

from django import forms

from .models import Memo


class MemoForm(forms.ModelForm):
    """ Form for Memo. """
    content = forms.CharField(
        widget=forms.Textarea(),
    )

    class Meta:
        model = Memo
        fields = [
            'content',
        ]
