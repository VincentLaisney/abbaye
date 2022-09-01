""" apps/agenda/forms.py """

from django import forms
from tempus_dominus.widgets import DatePicker

from .models import Event


class EventForm(forms.ModelForm):
    """ Form for Event. """
    name = forms.CharField(
        label='Nom :',
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
    category = forms.ChoiceField(
        label='Catégorie :',
        choices=[
            ('Conférence', 'Conférence'),
            ('Retraite', 'Retraite'),
            ('Promenade', 'Promenade'),
        ],
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )
    date_from = forms.DateField(
        label='Du :',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(options={
            'format': 'DD/MM/YYYY',
        }),
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
    date_to = forms.DateField(
        label='Au :',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(options={
            'format': 'DD/MM/YYYY',
        }),
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
    comment = forms.CharField(
        required=False,
        label='Remarques :',
        widget=forms.Textarea,
    )

    class Meta:
        model = Event
        fields = ('__all__')
