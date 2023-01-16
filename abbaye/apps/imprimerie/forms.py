""" apps/imprimerie/forms.py """

from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Memo


class MemoForm(forms.ModelForm):
    """ Form for Memo. """
    content = forms.CharField(
        widget=SummernoteWidget()
    )

    class Meta:
        model = Memo
        fields = [
            'content',
        ]
