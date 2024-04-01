""" apps/hotellerie/models.py """

import re
import datetime

from django.db import models


class Personne(models.Model):
    """ Personne model. """
    nom = models.CharField(
        max_length=255,
    )
    prenom = models.CharField(
        max_length=255,
    )
    moine_flav = models.BooleanField(
        default=False,
    )
    est_pere_suiveur = models.BooleanField(
        default=False,
    )
    qualite = models.CharField(
        max_length=25,
    )
    pere_suiveur = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    pretre = models.BooleanField(
        default=False,
    )
    messe_forme = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )
    messe_langue = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )
    commentaire = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        nom_complet = self.qualite
        nom_complet += ' ' if self.qualite or self.prenom else ''
        nom_complet += self.prenom if self.prenom else ''
        nom_complet += ' ' if self.prenom or self.nom else ''
        name = re.sub(
            r'^DE ',
            lambda match: 'de ',
            self.nom.upper()
        )
        name = re.sub(
            r'^D\'',
            lambda match: 'd\'',
            self.nom.upper()
        )
        nom_complet += name if self.nom else ''
        return nom_complet


class Mail(models.Model):
    """ Mail model. """
    personne = models.ForeignKey(
        to='Personne',
        on_delete=models.CASCADE,
        related_name='mail_personne',
    )
    mail = models.EmailField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.mail


class Telephone(models.Model):
    """ Telephone model. """
    personne = models.ForeignKey(
        to='Personne',
        on_delete=models.CASCADE,
        related_name='tel_personne',
    )
    num_tel = models.CharField(
        max_length=25,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.num_tel


class Adresse(models.Model):
    """ Adresse model. """
    personne = models.ForeignKey(
        to='Personne',
        on_delete=models.CASCADE,
        related_name='adresse_personne',
    )
    rue = models.TextField()
    code_postal = models.CharField(
        max_length=25,
    )
    ville = models.CharField(
        max_length=50,
    )
    pays = models.CharField(
        max_length=25,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        adresse_as_string = ''
        adresse_as_string += self.rue + ' | ' if self.rue else ''
        adresse_as_string += self.code_postal + ' | ' if self.code_postal else ''
        adresse_as_string += self.ville if self.ville else ''
        return adresse_as_string


class Sejour(models.Model):
    """ Sejour class. """
    personne = models.ForeignKey(
        to=Personne,
        on_delete=models.CASCADE,
    )
    sejour_du = models.DateField()
    sejour_au = models.DateField()
    repas_du = models.CharField(
        max_length=25,
    )
    repas_au = models.CharField(
        max_length=25,
    )
    mensa = models.CharField(
        max_length=25,
    )
    dit_messe = models.BooleanField(
        default=False,
    )
    # messe_lendemain = models.BooleanField(
    #     default=False,
    # )
    messe_premier_jour = models.BooleanField(
        default=False,
    )
    tour_messe = models.CharField(
        max_length=25,
    )
    servant = models.BooleanField(
        default=False,
    )
    oratoire = models.CharField(
        max_length=50,
        null=True,
    )
    commentaire_cuisine = models.TextField()
    commentaire_sacristie = models.TextField()
    mail_sacristie = models.BooleanField(
        default=False,
    )
    mail_pere_suiveur = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return 'Séjour de {} du {} ({}) au {} ({})'.format(
            self.personne,
            self.sejour_du.strftime('%d/%m/%Y'),
            self.repas_du,
            self.sejour_au.strftime('%d/%m/%Y') if self.sejour_au else '--',
            self.repas_au
        )

    def chambres_list(self):
        """ Returns the rooms of the Sejour as a list. """
        chambres_queryset = Chambre.objects.filter(
            sejour=self).values('chambre')
        chambres_list = []
        for chambre in chambres_queryset:
            chambres_list.append(chambre['chambre'])
        return chambres_list

    def chambres_string(self):
        """ Returns the rooms of the Sejour as a string. """
        chambres_string = ''
        for chambre in self.chambres_list():
            chambres_string += (', ' if chambres_string !=
                                '' else '') + chambre
        return chambres_string


class Chambre(models.Model):
    """ Chambre model. """
    sejour = models.ForeignKey(
        to='Sejour',
        on_delete=models.CASCADE,
    )
    chambre = models.CharField(
        max_length=25,
    )

    def __str__(self):
        return '{} ({})'.format(self.chambre, self.sejour.__str__())


class Parloir(models.Model):
    """ Parloir model. """
    personne_1 = models.ForeignKey(
        to=Personne,
        on_delete=models.CASCADE,
        related_name='parloir_personne_1',
    )
    personne_2 = models.ForeignKey(
        null=True,
        to=Personne,
        on_delete=models.CASCADE,
        related_name='parloir_personne_2',
    )
    personne_3 = models.ForeignKey(
        null=True,
        to=Personne,
        on_delete=models.CASCADE,
        related_name='parloir_personne_3',
    )
    date = models.DateField()
    REPAS_NAMES = [
        ('Non défini', '---------'),
        ('Petit déjeuner', 'Petit déjeuner'),
        ('Déjeuner', 'Déjeuner'),
        ('Dîner', 'Dîner'),
    ]
    repas = models.CharField(
        max_length=50,
        choices=REPAS_NAMES,
    )
    nombre = models.IntegerField(
        null=True,
    )
    PARLOIRS_NAMES = [
        ('Non défini', '---------'),
        ('Saint-Benoît', 'Saint-Benoît'),
        ('Saint-Ignace', 'Saint-Ignace'),
        ('Saint-Dominique', 'Saint-Dominique'),
        ('Parloir 1 vélux', 'Parloir 1 vélux'),
        ('Parloir 2 vélux', 'Parloir 2 vélux'),
        ('Salle de projection', 'Projection'),
    ]
    parloir = models.CharField(
        max_length=50,
        choices=PARLOIRS_NAMES,
    )
    repas_apporte = models.BooleanField(
        default=False,
    )
    remarque = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def moines_string(self):
        """ Returns the monks concerned by the parloir as a string. """
        moines = self.personne_1.__str__()
        moines += ' + ' + self.personne_2.__str__() if self.personne_2 else ''
        moines += ' + ' + self.personne_3.__str__() if self.personne_3 else ''
        return moines

    def __str__(self):
        return "{} le {}".format(
            self.moines_string(),
            self.date.strftime('%d/%m/%Y'),
        )


class Retreat(models.Model):
    """ Retreat model. """
    date_from = models.DateField()
    duration = models.IntegerField()

    def date_to(self):
        """ Returns the date_to of a retreat. """
        return self.date_from + datetime.timedelta(days=self.duration)

    def date_to_string(self):
        """ Returns the date_to as a string of a retreat. """
        return self.date_to().strftime('%d/%m/%Y')

    def __str__(self):
        return 'Retraite du {} au {}'.format(
            self.date_from.strftime('%d/%m/%Y'),
            self.date_to_string()
        )
