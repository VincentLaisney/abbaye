""" apps/moines/forms.py """

from django import forms


from .models import Monk


class MonkForm(forms.ModelForm):
    """ Monk form. """
    name = forms.CharField(
        max_length=255,
    )
    birthday = forms.DateField(
        input_formats=[
            '%d/%m/%Y',
        ],
    )
    entry = forms.DateField(
        input_formats=[
            '%d/%m/%Y',
        ],
    )
    rank = forms.IntegerField()
    habit = forms.DateField(
        input_formats=[
            '%d/%m/%Y',
        ],
    )
    profession_temp = forms.DateField(
        input_formats=[
            '%d/%m/%Y',
        ],
    )
    profession_perp = forms.DateField(
        input_formats=[
            '%d/%m/%Y',
        ],
    )
    priest = forms.DateField(
        input_formats=[
            '%d/%m/%Y',
        ],
    )
    death = forms.DateField(
        input_formats=[
            '%d/%m/%Y',
        ],
    )
    email = forms.EmailField()
    additional_email = forms.EmailField()
    is_active = forms.BooleanField()
    absences_recipient = forms.BooleanField()

    class Meta:
        model = Monk
        fields = '__all__'
