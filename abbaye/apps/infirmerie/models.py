""" apps/infirmerie/models.py """

from django.db import models

#from apps.moines.models import Monk


class Speciality(models.Model):
    """ Speciality model. """
    speciality = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.speciality


class Toubib(models.Model):
    """ Toubib model. """
    titre = models.CharField(
        max_length=25,
    )
    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=50,
    )
    # specialite = models.CharField(max_length=25)
    speciality = models.ForeignKey(
        to=Speciality,
        on_delete=models.CASCADE,
    )
    is_medecin = models.BooleanField()
    adresse_1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    adresse_2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    adresse_3 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    code_postal = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    ville = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    telephone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    remarques = models.TextField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(
        self
    ):
        nom_complet = self.titre
        nom_complet += ' ' if self.titre else ''
        nom_complet += self.first_name if self.first_name else ''
        nom_complet += ' ' if self.first_name else ''
        nom_complet += self.last_name.upper()

        return nom_complet

#     def get_absolute_url(
# self
# ):
#         """ Return absolute url. """
#         return reverse(
# 'toubibs:detail', args=[self.pk]
# )

    def adresse_complete(
        self
    ):
        """ Return complete address as text. """
        adresse_complete = ''
        adresse_complete += self.adresse_1 if self.adresse_1 else ''
        adresse_complete += '\n' if self.adresse_1 else '' + \
            self.adresse_2 if self.adresse_2 else ''
        adresse_complete += '\n' if self.adresse_2 else '' + \
            self.adresse_3 if self.adresse_3 else ''
        adresse_complete += '\n' if self.adresse_3 else '' + \
            self.code_postal if self.code_postal else ''
        adresse_complete += ' ' if self.code_postal else ''
        adresse_complete += self.ville if self.ville else ''

        return adresse_complete


class Billet(models.Model):
    """ Billet model. """
    titre = models.CharField(
        max_length=255,
    )
#    moine1 = models.ForeignKey(
#        Monk,
#        related_name='billets_moine1',
#        on_delete=models.CASCADE,
#    )
#    moine2 = models.ForeignKey(
#        Monk,
#        related_name='billets_moine2',
#        on_delete=models.CASCADE,
#        null=True,
#    )
#    moine3 = models.ForeignKey(
#        Monk,
#        related_name='billets_moine3',
#        on_delete=models.CASCADE,
#        null=True,
#    )
#    moine4 = models.ForeignKey(
#        Monk,
#        related_name='billets_moine4',
#        on_delete=models.CASCADE,
#        null=True,
#    )
#    chauffeur = models.ForeignKey(
#        Monk,
#        related_name='billets_chauffeur',
#        on_delete=models.CASCADE,
#        null=True,
#    )
    toubib = models.ForeignKey(
        Toubib,
        related_name='billets_toubib',
        on_delete=models.CASCADE,
    )
    when = models.DateTimeField()
    where = models.CharField(
        max_length=25,
    )
    prix = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2,
    )
    facture = models.BooleanField(
        default=False,
    )
    gratis = models.BooleanField(
        default=False,
    )
    vitale = models.BooleanField(
        default=False,
    )
    remarque = models.TextField(
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.titre

    def moines(self):
        """ Return a unique string of all the monks. """
        moines = ''
        moines += self.moine1
        moines += (', ' + self.moine2) if self.moine2 else ''
        moines += (', ' + self.moine3) if self.moine3 else ''
        moines += (', ' + self.moine4) if self.moine4 else ''

        return moines

    # def date_time(self):
    #     """ Return date and time of rendez-vous under human form. """
    #     return self.when.strftime('%d/%m/%Y') + ' à ' + self.when.strftime('%H:%M')
