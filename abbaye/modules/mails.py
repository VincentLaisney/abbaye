""" Module mails. """

import smtplib
from email.message import EmailMessage

from django.conf import settings

from modules.preferences import PREFERENCES

from apps.hotellerie.models import Mail, Personne


def mail_sacristie(sejour):
    """ Sends an email to sacristie and services. """
    priest = Personne.objects.get(pk=sejour.personne.pk)

    body = 'Mon cher Père,\n\n'
    body += 'Il va y avoir un prêtre-hôte :\n'
    body += '{}\n'.format(priest)
    body += 'Du : {}\n'.format(sejour.sejour_du)
    body += 'Au : {}\n'.format(sejour.sejour_au)
    body += 'Chambre : {}\n\n'.format(sejour.chambres_string())
    body += 'IL CÉLÉBRERA LA MESSE LE JOUR DE SON ARRIVÉE\n\n' \
        if sejour.messe_premier_jour \
        else 'Messe le lendemain de son arrivée\n\n'
    body += 'Forme : {}\n'.format(priest.messe_forme)
    body += 'Langue : {}\n'.format(priest.messe_langue)
    body += 'Tour de Messe : {}\n'.format(sejour.tour_messe)
    body += 'Attribuer un servant svp.\n' if sejour.servant else ''
    body += 'Oratoire : {}.\n\n'.format(
        sejour.oratoire if sejour.oratoire else 'NON DÉFINI')
    body += 'Commentaire : {}\n\n'.format(
        sejour.commentaire_sacristie) \
        if sejour.commentaire_sacristie else ''
    body += 'Bien à vous.\n'
    body += 'P. Martin Marie'

    #provisory solution for problem with django email
    send_a_mail(
        'MESSE : {}'.format(priest),
        body,
        PREFERENCES['mail_hotelier'],
        [
            PREFERENCES['mail_sacristain'],
            PREFERENCES['mail_reliques'],
            PREFERENCES['mail_services'],
        ],
    )


def mail_pere_suiveur(sejour):
    """ Sends an email to the Père suiveur. """
    guest = Personne.objects.get(pk=sejour.personne.pk)

    body = 'Cher Père,\n\n'
    body += '{} séjournera à l\'hôtellerie.\n\n'.format(guest)
    body += 'La chambre {} lui est attribuée.\n\n'.format(
        sejour.chambres_string())
    body += 'Il arrivera le {} ({})'.format(
        sejour.sejour_du,
        sejour.repas_du if sejour.repas_du != '---------' else 'repas non précisé'
    )
    body += ' et repartira le {} ({}).\n\n'.format(
        sejour.sejour_au,
        sejour.repas_au if sejour.repas_au != '---------' else 'repas non précisé'
    )
    body += 'Les frères de l\'hôtellerie l’accueilleront et vous préviendront lorsqu\'il sera installé.\n\n'
    body += 'In Domino.\n'
    body += 'Père Martin Marie'

    send_a_mail(
        'HÔTE : {}'.format(guest),
        body,
        PREFERENCES['mail_hotelier'],
        [', '.join(
            [str(mail)
             for mail in Mail.objects.filter(personne=guest.pere_suiveur)]
        )],
    )

def send_a_mail(subject, body, sender, dest):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = dest
    msg.set_content(body)

    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.starttls()
        server.send_message(msg)
