""" apps/editor/forms.py """

from django import forms

from .models import Collection, Interpreter, Product


class BookForm(forms.ModelForm):
    """ Form for Book. """
    category = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'value': 'book',
            }
        ),
    )
    ref_tm = forms.CharField(
        required=False,
        label='Réf. TM :',
        label_suffix='',
        help_text='Références existantes : ' +
        ', '.join(
            ref['ref_tm'] for ref in list(
                Product.objects
                .filter(category='book')
                .filter(ref_tm__isnull=False)
                .exclude(ref_tm='')
                .order_by('ref_tm')
                .values('ref_tm')
            )
        ),
    )
    ean = forms.CharField(
        required=False,
        label='EAN :',
        label_suffix='',
    )
    title = forms.CharField(
        required=False,
        label='Titre :',
        label_suffix='',
    )
    sub_title = forms.CharField(
        required=False,
        label='Sous-titre :',
        label_suffix='',
    )
    author = forms.CharField(
        required=False,
        label='Auteur :',
        label_suffix='',
    )
    collection = forms.ModelChoiceField(
        required=False,
        queryset=Collection.objects.all().order_by('name'),
        label='Collection :',
        label_suffix='',
    )
    number_in_collection = forms.IntegerField(
        required=False,
        label='Numéro dans la collection :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    circulation = forms.IntegerField(
        required=False,
        label='Tirage :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    publication = forms.DateField(
        required=False,
        label='Date de parution :',
        label_suffix='',
    )
    width = forms.IntegerField(
        required=False,
        label='Largeur (mm):',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    height = forms.IntegerField(
        required=False,
        label='Hauteur (mm):',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    number_of_pages = forms.IntegerField(
        required=False,
        label='Nombre de pages :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    weight = forms.IntegerField(
        required=False,
        label='Poids (g):',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    presentation_product = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        label='Présentation produit :',
        label_suffix='',
    )
    presentation_author = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        label='Présentation auteur :',
        label_suffix='',
    )
    strong_points = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        label='Points forts :',
        label_suffix='',
    )
    target_audience = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        label='Public visé :',
        label_suffix='',
    )
    coefficient = forms.FloatField(
        required=False,
        label='Coefficient :',
        label_suffix='',
        widget=forms.NumberInput(
            attrs={
                'placeholder': '6',
            }
        ),
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    price = forms.FloatField(
        required=False,
        label='Prix public :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    remarques = forms.CharField(
        required=False,
        label='Remarques :',
        label_suffix='',
        widget=forms.Textarea()
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'title',
            'sub_title',
            'author',
            'collection',
            'number_in_collection',
            'presentation_product',
            'presentation_author',
            'strong_points',
            'target_audience',
            'number_of_pages',
            'circulation',
            'publication',
            'width',
            'height',
            'weight',
            'coefficient',
            'price',
            'remarques',
        ]


class DiskForm(forms.ModelForm):
    """ Form for CD. """
    category = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'value': 'disk',
            }
        ),
    )
    ref_tm = forms.CharField(
        required=False,
        label='Réf. TM :',
        label_suffix='',
        help_text='Références existantes : ' +
        ', '.join(
            ref['ref_tm'] for ref in list(
                Product.objects
                .filter(category='disk')
                .filter(ref_tm__isnull=False)
                .exclude(ref_tm='')
                .order_by('ref_tm')
                .values('ref_tm')
            )
        ),
    )
    ean = forms.CharField(
        required=False,
        label='EAN :',
        label_suffix='',
    )
    title = forms.CharField(
        required=False,
        label='Titre :',
        label_suffix='',
    )
    sub_title = forms.CharField(
        required=False,
        label='Sous-titre :',
        label_suffix='',
    )
    interpreter = forms.ModelChoiceField(
        required=False,
        queryset=Interpreter.objects.all().order_by('name'),
        label='Interprète :',
        label_suffix='',
    )
    circulation = forms.IntegerField(
        required=False,
        label='Tirage :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },)
    publication = forms.DateField(
        required=False,
        label='Date de parution :',
        label_suffix='',
    )
    weight = forms.IntegerField(
        required=False,
        label='Poids (g):',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    coefficient = forms.FloatField(
        required=False,
        label='Coefficient :',
        label_suffix='',
        widget=forms.NumberInput(
            attrs={
                'placeholder': '6',
            }
        ),
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    pght = forms.FloatField(
        required=False,
        label='PGHT :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    remarques = forms.CharField(
        required=False,
        label='Remarques :',
        label_suffix='',
        widget=forms.Textarea()
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'title',
            'sub_title',
            'interpreter',
            'circulation',
            'publication',
            'weight',
            'coefficient',
            'pght',
            'remarques',
        ]


class ImageForm(forms.ModelForm):
    """ Form for Image. """
    category = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'value': 'image',
            }
        ),
    )
    ref_tm = forms.CharField(
        required=False,
        label='Réf. TM :',
        label_suffix='',
        help_text='Références existantes : ' +
        ', '.join(
            ref['ref_tm'] for ref in list(
                Product.objects
                .filter(category='image')
                .filter(ref_tm__isnull=False)
                .exclude(ref_tm='')
                .order_by('ref_tm')
                .values('ref_tm')
            )
        ),
    )
    ean = forms.CharField(
        required=False,
        label='EAN :',
        label_suffix='',
    )
    recto_img = forms.CharField(
        max_length=255,
        required=False,
        label='Recto :',
        label_suffix='',
    )
    verso_img = forms.CharField(
        required=False,
        max_length=255,
        label='Verso :',
        label_suffix='',
    )
    width = forms.IntegerField(
        required=False,
        label='Largeur (mm):',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    height = forms.IntegerField(
        required=False,
        label='Hauteur (mm):',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'recto_img',
            'verso_img',
            'width',
            'height',
        ]


class ChargeForm(forms.ModelForm):
    """ Form for Charges. """
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mx-1',
                'style': 'color: black; width: 120px',
                'placeholder': 'Charge',
            }
        ),
        label='Charge :',
        label_suffix='',
    )
    amount = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mx-1',
                'style': 'color: black; width: 100px',
                'placeholder': 'Montant',
            }
        ),
        label='Montant :',
        label_suffix='',
    )
