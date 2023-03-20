""" apps/moines/forms.py """

from django import forms

from .models import Monk


class MonkForm(forms.ModelForm):
    """ Monk form.
    Required fields: name and entry. """
    name = forms.CharField(
        max_length=255,
        label='Nom',
        label_suffix=' :',
    )
    feast_day = forms.ChoiceField(
        choices=[(i+1, i+1) for i in range(31)],
    )
    feast_month = forms.ChoiceField(
        choices=[
            (1, 'janvier'),
            (2, 'février'),
            (3, 'mars'),
            (4, 'avril'),
            (5, 'mai'),
            (6, 'juin'),
            (7, 'juillet'),
            (8, 'août'),
            (9, 'septembre'),
            (10, 'octobre'),
            (11, 'novembre'),
            (12, 'décembre'),
        ],
    )
    laundry_number = forms.IntegerField()
    phone_number = forms.IntegerField()
    birthday = forms.DateField(
        required=False,
        input_formats=[
            '%d/%m/%Y',
        ],
        label='Date de naissance',
        label_suffix=' :',
    )
    entry = forms.DateField(
        input_formats=[
            '%d/%m/%Y',
        ],
        label='Date d\'entrée',
        label_suffix=' :',
    )
    rank = forms.IntegerField(
        required=False,
        label='Rang',
        label_suffix=' :',
        help_text='Si plusieurs moines sont entrés le même jour, indiquez ici leur rang (1 pour le premier, 2 pour le deuxième etc.).',
        initial=1,
    )
    habit = forms.DateField(
        required=False,
        input_formats=[
            '%d/%m/%Y',
        ],
        label='Date de prise d\'habit',
        label_suffix=' :',
    )
    profession_temp = forms.DateField(
        required=False,
        input_formats=[
            '%d/%m/%Y',
        ],
        label='Date de profession temporaire',
        label_suffix=' :',
    )
    profession_perp = forms.DateField(
        required=False,
        input_formats=[
            '%d/%m/%Y',
        ],
        label='Date de profession perpétuelle',
        label_suffix=' :',
    )
    priest = forms.DateField(
        required=False,
        input_formats=[
            '%d/%m/%Y',
        ],
        label='Date d\'ordination sacerdotale',
        label_suffix=' :',
    )
    death = forms.DateField(
        required=False,
        input_formats=[
            '%d/%m/%Y',
        ],
        label='Date de décès',
        label_suffix=' :',
    )
    email = forms.EmailField(
        required=False,
        label='Email',
        label_suffix=' :',
    )
    additional_email = forms.EmailField(
        required=False,
        label='Email supplémentaire',
        label_suffix=' :',
    )
    is_active = forms.BooleanField(
        required=False,
        label='Est actif',
        label_suffix='',
    )
    absences_recipient = forms.BooleanField(
        required=False,
        label='Destinataire ex officio des avis d\'absence',
        label_suffix='',
    )

    class Meta:
        model = Monk
        fields = '__all__'
