""" apps/polyglotte/forms.py """

from django import forms

from .models import Verse


class VerseForm(forms.ModelForm):
    """ Verse form. """
    attrs_textarea = {'cols': 60, 'rows': 3}
    txt_hebrew = forms.CharField(
        required=False,
        label='Hébreu :',
        widget=forms.Textarea(attrs=attrs_textarea)
    )
    txt_greek = forms.CharField(
        required=False,
        label='Grec :',
        widget=forms.Textarea(attrs=attrs_textarea)
    )
    txt_latin = forms.CharField(
        required=True,
        label='Latin :',
        widget=forms.Textarea(attrs=attrs_textarea)
    )

    class Meta:
        model = Verse
        fields = ('txt_hebrew', 'txt_greek', 'txt_latin')
