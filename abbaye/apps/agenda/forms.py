""" apps/agenda/forms.py """

from django import forms

from .models import Category, Event


class EventForm(forms.ModelForm):
    """ Form for Event. """
    name = forms.CharField(
        label='Nom :',
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
    category = forms.ModelChoiceField(
        label='Catégorie :',
        queryset=Category.objects.all().order_by('name'),
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )
    date_from = forms.DateField(
        label='Du :',
        input_formats=[
            '%d/%m/%Y',
        ],
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
    date_to = forms.DateField(
        label='Au :',
        input_formats=[
            '%d/%m/%Y',
        ],
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
