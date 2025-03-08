""" apps/infirmerie/forms.py """

from django import forms
from django.core.mail import send_mail
from dal import autocomplete

from .models import Billet, Speciality, Toubib

#from apps.moines.models import Moine

#from tempus_dominus.widgets import DateTimePicker



class ToubibForm(forms.ModelForm):
    """ Toubib form. """
    titre = forms.ChoiceField(
        label='Qualité :',
        choices=[
            ('Dr', 'Docteur'),
            ('M.', 'Monsieur'),
            ('Mme', 'Madame'),
        ],
        error_messages={
            'required': 'Ce champ est obligatoire.',
        }
    )
    nom = forms.CharField(
        label='Nom :',
        error_messages={
            'required': 'Ce champ est obligatoire.',
        }
    )
    prenom = forms.CharField(
        required=False,
        label='Prénom :',
    )
    speciality = forms.ModelChoiceField(
        label='Spécialité :',
        queryset=Speciality.objects.all().order_by('speciality'),
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )
    is_medecin = forms.BooleanField(
        required=False,
        label='Est médecin',
        label_suffix='',
    )
    adresse_1 = forms.CharField(
        required=False,
        label='Adresse 1 :',
    )
    adresse_2 = forms.CharField(
        required=False,
        label='Adresse 2 :',
    )
    adresse_3 = forms.CharField(
        required=False,
        label='Adresse 3 :',
    )
    code_postal = forms.CharField(
        required=False,
        label='Code postal :',
    )
    ville = forms.CharField(
        required=False,
        label='Ville :',
    )
    telephone = forms.CharField(
        required=False,
        label='Téléphone :',
    )
    email = forms.EmailField(
        required=False,
        label='Mail :',
        error_messages={
            'invalid': 'Adresse mail invalide.',
        }
    )
    remarques = forms.CharField(
        required=False,
        label='Remarques',
        widget=forms.Textarea,
    )

    class Meta:
        model = Toubib
        fields = ['titre', 'nom', 'prenom', 'speciality', 'is_medecin', 'adresse_1', 'adresse_2',
                  'adresse_3', 'code_postal', 'ville', 'telephone', 'email', 'remarques']


class SpecialityForm(forms.ModelForm):
    """ Form for speciality. """
    speciality = forms.CharField(
        label='Nom de la spécialité :',
        label_suffix='',
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )

    class Meta:
        model = Speciality
        fields = ['speciality']

class BilletForm(forms.ModelForm):
    """ Billet form. """
    titre = forms.CharField(
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        help_text='Par exemple "P. Vianney (ophtalmo)"',
    )
#    when = forms.DateTimeField(
#        label='Date et heure :',
#        input_formats=[
#            '%d/%m/%Y %H:%M',
#        ],
#        widget=DateTimePicker(
#            options={
#                'format': 'DD/MM/YYYY HH:mm',
#                'locale': 'fr',
#                'sideBySide': True,
#            },
#        ),
#        error_messages={
#            'invalid': 'Date invalide.',
#            'required': 'Ce champ est obligatoire',
#        }
#    )
    where = forms.ChoiceField(
        choices=[
            ('Travail', 'Travail'),
            ('Domicile', 'Domicile'),
            ('Infirmerie', 'Infirmerie'),
            ('Porterie', 'Porterie'),
        ],
        label='Lieu :',
    )
#    moine1 = forms.ModelChoiceField(
#        queryset=Moine.objects.all().order_by('nom_religieux'),
#        label='Moine 1 :',
#        error_messages={
#            'required': 'Ce champ est obligatoire',
#        },
#    )
#    moine2 = forms.ModelChoiceField(
#        required=False,
#        queryset=Moine.objects.all().order_by('nom_religieux'),
#        label='Moine 2 :',
#    )
#    moine3 = forms.ModelChoiceField(
#        required=False,
#        queryset=Moine.objects.all().order_by('nom_religieux'),
#        label='Moine 3 :',
#    )
#    moine4 = forms.ModelChoiceField(
#        required=False,
#        queryset=Moine.objects.all().order_by('nom_religieux'),
#        label='Moine 4 :',
#    )
#    chauffeur = forms.ModelChoiceField(
#        required=False,
#        queryset=Moine.objects.filter(
#            is_chauffeur=True).order_by('nom_religieux'),
#        label='Chauffeur :',
#    )
    prix = forms.FloatField(
        required=False,
        label='Prix :',
        widget=forms.TextInput,
        help_text='NB : Les éventuelles virgules sont automatiquement converties en points.',
    )
    facture = forms.BooleanField(
        required=False,
        label='Facture',
        label_suffix='',
    )
    gratis = forms.BooleanField(
        required=False,
        label='Gratis',
        label_suffix='',
    )
    vitale = forms.BooleanField(
        required=False,
        label='Carte vitale',
        label_suffix='',
    )
    toubib = forms.ModelChoiceField(
        label='Médecin :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        help_text='Entrez les premières lettres du nom du médecin.',
        queryset=Toubib.objects.all(),
        widget=autocomplete.ModelSelect2(url='toubibs:autocomplete'),
    )
    remarque = forms.CharField(
        required=False,
        label='Remarques :',
        widget=forms.Textarea,
    )

    class Meta:
        model = Billet
        fields = ('__all__')

    def send_email(self):
        """ Send email to courses. """
        # Subject:
        mail_subject = 'RV médical (' + self.instance.titre + ')'
        # Message:
        mail_message = ''
        mail_message += 'Date et heure : ' + self.instance.date_time()
        mail_message += '\nVille : ' + self.instance.toubib.ville
        mail_message += '\nMoines : ' + self.instance.moines()
        mail_message += '\nMédecin : ' + self.instance.toubib.__str__()
        mail_message += ('\nChauffeur : ' + self.instance.chauffeur.__str__()
                         ) if self.instance.chauffeur else ''
        if self.instance.gratis:
            mail_message += '\nGratis pro Deo'
        elif self.instance.prix:
            mail_message += '\nPrix : ' + \
                (' {:.2f} €'.format(self.instance.prix)
                 if str(self.instance.prix - int(self.instance.prix))[1:] != '.0'
                 else ' {:.0f} €'.format(self.instance.prix))
        mail_message += '\nFacture' if self.instance.facture else ''
        mail_message += '\n---------------------'
        mail_message += '\nMessage envoyé depuis http://python.asj.com:8001'
        # From:
        mail_from = 'infirmier@clairval.com'
        # To:
        mail_to = [
            'infirmier@traditions-monastiques.com',
            'courses@clairval.com'
        ]

        send_mail(mail_subject, mail_message, mail_from, mail_to)
