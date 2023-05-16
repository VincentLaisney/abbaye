""" apps/imprimerie/forms.py """

from django import forms

from .models import Memo, Client, Paper, Project, Element


class MemoForm(forms.ModelForm):
    """ Form for Memo. """
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 20,
            }
        )
    )

    class Meta:
        model = Memo
        fields = [
            'content',
        ]
