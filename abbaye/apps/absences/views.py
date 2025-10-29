""" apps/absences/views.py """

import smtplib
from email.message import EmailMessage

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import TicketForm
from .models import Monk, Ticket


def list(request, *args, **kwargs):
    """ List of Tickets (home page of Absences). """
    tickets = Ticket.objects.all().order_by('-go_date', '-back_date')[:50]
    return render(
        request,
        'absences/list.html',
        {
            'tickets': tickets,
        },
    )


def create(request):
    """ Create ticket. """
    mandatory_recipients = mandatory_recipients_queryset()

    if request.method == 'POST':
        data = request.POST
        form = TicketForm(data)
        additional_recipients = dict(data)['additional_recipients'] \
            if 'additional_recipients' in dict(data).keys() else []
        if form.is_valid():
            form.save()
            send_email(
                data,
                dict(data)['monks'],
                mandatory_recipients,
                additional_recipients,
            )
            return HttpResponseRedirect(reverse('absences:list'))

    else:
        form = TicketForm()

    return render(
        request,
        'absences/form.html',
        {
            'form': form,
            'mandatory_recipients': mandatory_recipients,
        }
    )


def details(request, *args, **kwargs):
    """ Details of a ticket. """
    ticket = get_object_or_404(Ticket, pk=kwargs['pk'])
    mandatory_recipients = '</br>'.join(
        monk.__str__() + ' (' + monk.email + ')'
        for monk in mandatory_recipients_queryset()
    )
    additional_recipients = ticket.additional_recipients_as_string()
    return render(
        request,
        'absences/details.html',
        {
            'ticket': ticket,
            'mandatory_recipients': mandatory_recipients,
            'additional_recipients': additional_recipients,
        },
    )


def update(request, *args, **kwargs):
    """ Update a ticket. """
    ticket = get_object_or_404(Ticket, pk=kwargs['pk'])
    mandatory_recipients = mandatory_recipients_queryset()

    if request.method == 'POST':
        data = request.POST
        form = TicketForm(data, instance=ticket)
        additional_recipients = dict(data)['additional_recipients'] \
            if 'additional_recipients' in dict(data).keys() else []
        if form.is_valid():
            form.save()
            send_email(
                data,
                dict(data)['monks'],
                mandatory_recipients,
                additional_recipients,
                'update'
            )
            return HttpResponseRedirect(reverse('absences:list'))

    else:
        form = TicketForm(instance=ticket)

    return render(
        request,
        'absences/form.html',
        {
            'form': form,
            'ticket': ticket,
            'mandatory_recipients': mandatory_recipients,
        }
    )


def delete(request, *args, **kwargs):
    """ Delete a ticket. """
    ticket = get_object_or_404(Ticket, pk=kwargs['pk'])

    if request.method == 'POST':
        data = ticket.__dict__
        # TODO: No other solution that formatting dates?
        data['go_date'] = '{:02}/{:02}/{:04}'.format(
            data['go_date'].day,
            data['go_date'].month,
            data['go_date'].year
        )
        data['back_date'] = '{:02}/{:02}/{:04}'.format(
            data['back_date'].day,
            data['back_date'].month,
            data['back_date'].year
        )
        monks = ticket.monks.all() \
            .order_by('entry', 'rank_entry') \
            .values_list('pk', flat=True)
        mandatory_recipients = mandatory_recipients_queryset()
        additional_recipients = ticket.additional_recipients.all() \
            .order_by('entry', 'rank_entry') \
            .values_list('pk', flat=True)
        form = TicketForm(request.POST, instance=ticket)
        # TODO: How to delete ticket before sending mail without losing data?
        send_email(
            data,
            monks,
            mandatory_recipients,
            additional_recipients,
            'delete'
        )
        ticket.delete()
        return HttpResponseRedirect(reverse('absences:list'))

    form = TicketForm(instance=ticket)

    return render(
        request,
        'absences/delete.html',
        {
            'form': form,
            'ticket': ticket,
        },
    )


def mandatory_recipients_queryset():
    """ Queryset: all the mandatory recipients. """
    return Monk.objects \
        .filter(absences_recipient=True) \
        .filter(is_active=True) \
        .order_by('absolute_rank', 'entry', 'rank_entry')


def send_email(data, monks, mandatory_recipients, additional_recipients, action=''):
    """ Send email with data. """
    monks = ', '.join([Monk.objects.get(pk=monk).__str__() for monk in monks])
    mandatory_recipients_email = [
        recipient.email for recipient in mandatory_recipients
    ]
    additional_recipients_emails = [
        Monk.objects.get(pk=additional_recipient).email
        for additional_recipient in additional_recipients
    ]
    recipients_emails = mandatory_recipients_email + additional_recipients_emails
    avis = 'AVIS D\'ABSENCE' if data['type'] == 'out' else 'AVIS DE RETOUR'
    if action == 'update':
        subject = '{} ***MODIFIÉ***'.format(avis)
        body = '!!! {} MODIFIÉ !!!\n\n'.format(avis)
    elif action == 'delete':
        subject = '{} ***SUPPRIMÉ***'.format(avis)
        body = 'CET {} EST SUPPRIMÉ :\n\n'.format(avis)
    else:
        subject = '{}'.format(avis)
        body = ''
    body += write_body(data, monks, action)
    body += '\n\n{}'.format(''.join(['-'] * 72))
    body += '\nCe message vous a été envoyé depuis http://python.asj.com:8011/abbaye/absences/.'
    body += '\n{}'.format(''.join(['-'] * 72))
    return send_a_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        recipients_emails,
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

def write_body(data, monks, action):
    """ Write the body of the mail. """
    body = ''
    # Monks
    body += 'Moines concernés : {}'.format(monks)

    # Destination:
    body += '\n\nDestination : {}' \
        .format(data['destination']) if data['destination'] else ''

    # Go:
    go = 'DÉPART' if data['type'] == 'out' else 'RETOUR'
    back = 'RETOUR' if data['type'] == 'out' else 'DÉPART'
    body += '\n\n{} : {}' \
        .format(go, data['go_date'])
    body += ' ({})' \
        .format(data['go_moment'].lower()) if data['go_moment'] else ''
    body += ' en {}.' \
        .format(data['go_by'].lower()) if data['go_by'] else ''
    body += '\nGare : {}' \
        .format(data['go_station']) if data['go_station'] else ''
    body += ' à {}' \
        .format(data['go_hour']) if data['go_hour'] else ''
    body += '\n  + Repas avec les serveurs' \
        if 'servants' in data.keys() and data['servants'] else ''
    body += '\n  + Casse-croûte' \
        if 'picnic' in data and data['picnic'] else ''

    # Back:
    body += '\n\n{} : {}' \
        .format(back, data['back_date'])
    body += ' ({})' \
        .format(data['back_moment'].lower()) if data['back_moment'] else ''
    body += ' en {}.' \
        .format(data['back_by'].lower()) if data['back_by'] else ''
    body += '\nGare : {}' \
        .format(data['back_station']) if data['back_station'] else ''
    body += ' à {}' \
        .format(data['back_hour']) if data['back_hour'] else ''
    body += '\n  + Garder du chaud' \
        if 'keep_hot' in data and data['keep_hot'] else ''

    # Ordinary form:
    body += '\n\nMesse : forme ordinaire' \
        if 'ordinary_form' in data and data['ordinary_form'] else ''

    # Commentary:
    body += '\n\nCommentaire :\n{}' \
        .format(data['commentary']) if data['commentary'] else ''

    return body
