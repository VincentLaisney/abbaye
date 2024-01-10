""" apps/imprimerie/forms.py """

from django import forms
from dal import autocomplete

from .models import Work, Memo, Client, Paper, Project, Element


class WorkForm(forms.ModelForm):
    """ Form for Work. """
    class Meta:
        model = Work
        fields = [
            'content',
        ]


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
        widget=forms.Textarea(),
    )

    class Meta:
        model = Project
        fields = '__all__'


class ElementForm(forms.ModelForm):
    """ Form for Element. """
    name = forms.CharField(
        label='Nom de l\'élément :',
    )
    quantity = forms.IntegerField(
        label='Quantité :',
        required=False,
        initial=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    fixed = forms.FloatField(
        label='Frais fixes (€) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    notes = forms.CharField(
        label='Notes :',
        required=False,
        widget=forms.Textarea(
            attrs={
                'rows': 4,
            },
        ),
    )
    paper = forms.ModelChoiceField(
        label='Papier :',
        queryset=Paper.objects.all().order_by('name'),
        widget=autocomplete.ModelSelect2(
            url='imprimerie:papers_autocomplete',
        ),
        required=False,
    )
    paper_cut_into = forms.IntegerField(
        label='Papier coupé en :',
        required=False,
        initial=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    paper_dim1_machine = forms.FloatField(
        label='Papier dim. 1 (mm) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    paper_dim2_machine = forms.FloatField(
        label='Papier dim. 2 (mm) :',
        required=False,
        initial=0,
        help_text='Rappel: cette dimension donne le sens des fibres.',
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    file_width = forms.FloatField(
        label='Largeur du fichier (mm) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    file_height = forms.FloatField(
        label='Hauteur du fichier (mm) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    margins = forms.FloatField(
        label='Marges (mm) :',
        required=False,
        initial=20,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    gutters = forms.FloatField(
        label='Gouttières (mm) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    number_of_pages_doc = forms.IntegerField(
        label='Nb de feuilles du doc. :',
        required=False,
        initial=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    fibers = forms.BooleanField(
        label='Sens des fibres',
        label_suffix='',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'style': 'margin: 0 5px 0 0;'
            },
        ),
    )
    imposition = forms.IntegerField(
        label='Imposition :',
        required=False,
        initial=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    recto_verso = forms.BooleanField(
        label='Recto-verso',
        label_suffix='',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'style': 'margin: 0 5px 0 0;'
            },
        ),
    )
    color = forms.ChoiceField(
        label='Couleur :',
        choices=[
            ('B&W', 'Noir'),
            ('CMYN', 'CMJN'),
        ],
        required=False,
        widget=forms.Select(
            attrs={
                'style': 'margin: 0 0 0 5px;'
            },
        ),
    )
    massicot = forms.IntegerField(
        label='Massicot (min) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    pelliculage = forms.IntegerField(
        label='Pelliculage (min) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    rainage = forms.IntegerField(
        label='Rainage (min) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    encollage = forms.IntegerField(
        label='Encollage (min) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )
    agrafage = forms.IntegerField(
        label='Agrafage (min) :',
        required=False,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number',
            },
        )
    )

    class Meta:
        model = Element
        fields = '__all__'
