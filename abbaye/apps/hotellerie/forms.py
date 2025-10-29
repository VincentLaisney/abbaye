""" apps/hotellerie/forms.py """

from django import forms
from dal import autocomplete

from .models import Personne
from .models import Sejour
from .models import Parloir
from .models import Retreat


class PersonneForm(forms.ModelForm):
    """ Form for Personnes. """
    qualite = forms.ChoiceField(
        label='Qualité :',
        choices=[
            ('Abbé', 'Abbé'),
            ('Abbés', 'Abbés'),
            ('Brother', 'Brother'),
            ('Capitaine', 'Capitaine'),
            ('Cardinal', 'Cardinal'),
            ('Chanoine', 'Chanoine'),
            ('Colonel', 'Colonel'),
            ('Commandant', 'Commandant'),
            ('Docteur', 'Docteur'),
            ('Dom', 'Dom'),
            ('Don', 'Don'),
            ('Famille', 'Famille'),
            ('Father', 'Father'),
            ('Frère', 'Frère'),
            ('Frères', 'Frères'),
            ('Général', 'Général'),
            ('Le Comte', 'Le Comte'),
            ('Le TRP Abbé', 'Le TRP Abbé'),
            ('M. l\'Abbé', 'M. l\'Abbé'),
            ('M. le chanoine', 'M. le chanoine'),
            ('Madame', 'Madame'),
            ('Mademoiselle', 'Mademoiselle'),
            ('Mère', 'Mère'),
            ('Messieurs', 'Messieurs'),
            ('Monseigneur', 'Monseigneur'),
            ('Monsieur', 'Monsieur'),
            ('Monsieur et Madame', 'Monsieur et Madame'),
            ('Père', 'Père'),
            ('Pères', 'Pères'),
            ('Princesse', 'Princesse'),
            ('Professeur', 'Professeur'),
            ('Rev. Father', 'Rev. Father'),
            ('Révérendes Mères', 'Révérendes Mères'),
            ('RP.', 'RP.'),
            ('Sig.', 'Sig.'),
            ('Sœur', 'Sœur'),
            ('Sœurs', 'Sœurs'),
            ('TR PERE', 'TR PERE'),
        ],
        initial='Monsieur',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )
    nom = forms.CharField(
        required=False,
        label='Nom :',
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
    prenom = forms.CharField(
        required=False,
        label='Prénom :',
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire.',
        },
    )
    moine_flav = forms.BooleanField(
        required=False,
        label='Est un moine de Flavigny',
        label_suffix=''
    )
    est_pere_suiveur = forms.BooleanField(
        required=False,
        label='Est un Père suiveur',
        label_suffix=''
    )
    pere_suiveur = forms.ModelChoiceField(
        required=False,
        queryset=Personne.objects.filter(
            est_pere_suiveur=True).order_by('prenom'),
        label='Père suiveur :',
    )
    pretre = forms.BooleanField(
        required=False,
        label='Est un prêtre',
        label_suffix='',
    )
    messe_forme = forms.ChoiceField(
        required=False,
        label='Messe - forme :',
        choices=[
            ('', '---------'),
            ('Ordinaire', 'Ordinaire'),
            ('Extraordinaire', 'Extraordinaire'),
        ],
    )
    messe_langue = forms.ChoiceField(
        required=False,
        label='Messe - langue :',
        choices=[
            ('', '---------'),
            ('Français', 'Français'),
            ('Latin', 'Latin'),
            ('Anglais', 'Anglais'),
            ('Allemand', 'Allemand'),
            ('Espagnol', 'Espagnol'),
            ('Néerlandais', 'Néerlandais'),
        ],
    )
    commentaire = forms.CharField(
        required=False,
        label='Remarques',
        widget=forms.Textarea,
    )

    class Meta:
        model = Personne
        fields = ['qualite', 'nom', 'prenom', 'commentaire',
                  'moine_flav', 'est_pere_suiveur', 'pere_suiveur',
                  'pretre', 'messe_forme', 'messe_langue']


class MailForm(forms.ModelForm):
    """ Form for Mails. """
    mail = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 250px',
            }
        )
    )


class TelephoneForm(forms.ModelForm):
    """ Form for Telephones. """
    num_tel = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 150px',
            }
        )
    )


class AdresseForm(forms.ModelForm):
    """ Form for Adresses. """
    rue = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label_suffix='',
    )
    code_postal = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 100px',
            }
        ),
        label_suffix='',
    )
    ville = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 150px',
            }
        ),
        label_suffix='',
    )
    pays = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 150px',
            }
        ),
        label_suffix='',
    )


class SejourForm(forms.ModelForm):
    """ Form for Sejours. """
    personne = forms.ModelChoiceField(
        label='Personne :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        queryset=Personne.objects.all(),
        # widget=autocomplete.ModelSelect2(
        #     url='hotellerie:personnes_autocomplete_hotes'),
    )
    sejour_du = forms.DateField(
        label='Du :',
    )
    sejour_au = forms.DateField(
        label='Au :',
        required=False,
    )
    repas_du = forms.ChoiceField(
        choices=[
            ('Petit-déjeuner', 'Petit-déjeuner'),
            ('Déjeuner', 'Déjeuner'),
            ('Dîner', 'Dîner'),
        ],
    )
    repas_au = forms.ChoiceField(
        choices=[
            ('Petit-déjeuner', 'Petit-déjeuner'),
            ('Déjeuner', 'Déjeuner'),
            ('Dîner', 'Dîner'),
        ],
    )
    chambre = forms.MultipleChoiceField(
        required=False,
        label='Chambres :',
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'list-unstyled',
            },
        ),
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
            ('24', '24'),
            ('25', '25'),
            ('26', '26'),
            ('Chambre de l\'évêque', 'CE'),
        ],
    )
    mensa = forms.ChoiceField(
        label="Table",
        choices=[
            ('Sans repas', 'Sans repas'),
            ('Hôtes', 'Table des hôtes'),
            ('Table abbatiale', 'Table abbatiale'),
            ('Moines', 'Table des moines'),
            ('Parloirs', 'Repas aux parloirs'),
        ],
        initial='Hôtes',
    )
    dit_messe = forms.BooleanField(
        label='Prêtre avec Messe',
        label_suffix='',
        required=False,
    )
    # messe_lendemain = forms.BooleanField(
    #     label='Aura dit la Messe à son arrivée',
    #     label_suffix='',
    #     required=False,
    # )
    messe_premier_jour = forms.BooleanField(
        label='Dira la Messe le premier jour',
        label_suffix='',
        required=False,
    )
    tour_messe = forms.ChoiceField(
        label='Tour de Messe :',
        required=False,
        choices=[
            ('', '---------'),
            ('1er tour', '1er tour'),
            ('2e tour', '2e tour'),
            ('Matinée', 'Matinée'),
        ],
    )
    servant = forms.BooleanField(
        label='Attribuer un servant',
        label_suffix='',
        required=False,
    )
    oratoire = forms.ChoiceField(
        label='Oratoire :',
        required=False,
        choices=[
            ('', '---------'),
            ('Reliques', 'Reliques'),
            ('Salette', 'Salette'),
            ('Notre-Dame', 'Notre-Dame'),
            ('Saint-Jérôme', 'Saint-Jérôme'),
            ('Saint-Thomas', 'Saint-Thomas'),
            ('2e étage', '2e étage'),
            ('Saint-Joseph', 'Saint-Joseph'),
        ],
    )
    mail_sacristie = forms.BooleanField(
        label='Envoyer un mail à la sacristie',
        label_suffix='',
        required=False,
    )
    mail_pere_suiveur = forms.BooleanField(
        label='Envoyer un mail au Père suiveur',
        label_suffix='',
        required=False,
    )
    commentaire_cuisine = forms.CharField(
        required=False,
        label='Remarques pour la cuisine :',
        widget=forms.Textarea(
            attrs={
                'rows': 4,
            }
        ),
    )
    commentaire_sacristie = forms.CharField(
        required=False,
        label='Remarques pour la sacristie :',
        widget=forms.Textarea(
            attrs={
                'rows': 4,
            }
        ),
    )
    commentaire_listing = forms.CharField(
        required=False,
        label='Commentaire pour le listing :',
        widget=forms.Textarea(
            attrs={
                'rows': 4,
            }
        ),
    )

    class Meta:
        model = Sejour
        fields = ('__all__')


class ParloirForm(forms.ModelForm):
    """ Form for Parloirs. """
    personne_1 = forms.ModelChoiceField(
        label='Moine 1 :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        queryset=Personne.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='hotellerie:personnes_autocomplete_monks'),
    )
    personne_2 = forms.ModelChoiceField(
        label='Moine 2 :',
        required=False,
        queryset=Personne.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='hotellerie:personnes_autocomplete_monks'),
    )
    personne_3 = forms.ModelChoiceField(
        label='Moine 3 :',
        required=False,
        queryset=Personne.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='hotellerie:personnes_autocomplete_monks'),
    )
    date = forms.DateField(
        label='Date :',
    )
    repas = forms.ChoiceField(
        choices=[
            ('Non défini', '---------'),
            ('Petit déjeuner', 'Petit déjeuner'),
            ('Déjeuner', 'Déjeuner'),
            ('Dîner', 'Dîner'),
        ],
    )
    nombre = forms.IntegerField(
        initial=0,
        help_text="Nombre de personnes en plus des personnes ci-dessus",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 0,
            }
        )
    )
    parloir = forms.ChoiceField(
        label="Parloir :",
        choices=[
            ('Non défini', '---------'),
            ('Saint-Benoît', 'Saint-Benoît'),
            ('Saint-Ignace', 'Saint-Ignace'),
            ('Saint-Dominique', 'Saint-Dominique'),
            ('Parloir 1 vélux', 'Parloir 1 vélux'),
            ('Parloir 2 vélux', 'Parloir 2 vélux'),
            ('Salle de projection', 'Projection'),
        ],
    )
    repas_apporte = forms.BooleanField(
        required=False,
        label='Repas apporté',
        label_suffix='',
    )
    remarque = forms.CharField(
        required=False,
        label='Remarques :',
        widget=forms.Textarea,
    )

    class Meta:
        model = Parloir
        fields = ('__all__')


class RetreatForm(forms.ModelForm):
    """ Form for Personnes. """
    date_from = forms.DateField(
        label='Date :',
    )
    duration = forms.IntegerField(
        label='Durée :',
        label_suffix='',
        initial=5,
    )

    class Meta:
        model = Retreat
        fields = ['date_from', 'duration']
