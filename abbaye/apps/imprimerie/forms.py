""" apps/imprimerie/forms.py """

from django import forms
from dal import autocomplete

from .models import Client, Memo, Paper, Project


class MemoForm(forms.ModelForm):
    """ Form for Memo. """
    class Meta:
        model = Memo
        fields = [
            'content',
        ]


class ClientForm(forms.ModelForm):
    """ Form for Client. """
    quality = forms.CharField(
        label='Qualité :',
        required=False,
    )
    first_name = forms.CharField(
        label='Prénom :',
        widget=forms.TextInput(),
        required=False,
    )
    last_name = forms.CharField(
        label='Nom :',
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
        widget=forms.TextInput(),
    )
    address1 = forms.CharField(
        label='Adresse 1 :',
        widget=forms.TextInput(),
        required=False,
    )
    address2 = forms.CharField(
        label='Adresse 2 :',
        widget=forms.TextInput(),
        required=False,
    )
    address3 = forms.CharField(
        label='Adresse 3 :',
        widget=forms.TextInput(),
        required=False,
    )
    zip = forms.CharField(
        label='Code postal :',
        widget=forms.TextInput(),
        required=False,
    )
    city = forms.CharField(
        label='Ville :',
        widget=forms.TextInput(),
        required=False,
    )

    class Meta:
        model = Client
        fields = '__all__'


class PaperForm(forms.ModelForm):
    """ Form for Paper. """
    name = forms.CharField(
        label='Nom (marque) :',
    )
    dim1 = forms.CharField(
        label='Dimension 1 :',
    )
    dim2 = forms.CharField(
        label='Dimension 2 :',
        help_text='Rappel: cette dimension donne le sens des fibres.'
    )
    weight = forms.IntegerField(
        label='Grammage :',
    )
    price = forms.DecimalField(
        label='Prix au mille :',
        required=False,
    )

    class Meta:
        model = Paper
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    """ Form for Project. """
    name = forms.CharField(
        label='Nom :',
    )
    client = forms.ModelChoiceField(
        label='Client :',
        queryset=Client.objects.all().order_by('last_name', 'first_name'),
        widget=autocomplete.ModelSelect2(
            url='imprimerie:clients_autocomplete'
        ),
    )
    notes = forms.CharField(
        label='Notes :',
        required=False,
    )

    class Meta:
        model = Project
        fields = '__all__'
