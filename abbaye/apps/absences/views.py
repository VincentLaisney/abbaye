""" apps/absences/views.py """


from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import TicketForm
from .models import Monk, Ticket


def home(request):
    """ Home page of Absences. """
    tickets = Ticket.objects.all().order_by('-go_date', '-back_date')
    return render(
        request,
        'absences/home.html',
        {
            'tickets': tickets,
        },
    )


def success(request):
    """ Success view. """
    return render(
        request,
        'absences/home.html',
        {
            'title': 'success',
        },
    )


def failure(request):
    """ Failure view. """
    return render(
        request,
        'absences/home.html',
        {
            'title': 'failure',
        },
    )


def create(request):
    """ Create ticket. """
    mandatory_recipients = Monk.objects \
        .filter(absences_recipient=True) \
        .filter(is_active=True) \
        .order_by('entry', 'rank')

    if request.method == 'POST':
        data = request.POST
        form = TicketForm(data)
        additional_recipients = dict(data)['additional_recipients'] \
            if 'additional_recipients' in dict(data).keys() else []
        if form.is_valid():
            form.save()
            if send_email(
                data,
                dict(data)['monks'],
                mandatory_recipients,
                additional_recipients,
            ):
                return HttpResponseRedirect(
                    reverse(
                        'absences:success',
                    )
                )
            return HttpResponseRedirect(
                reverse(
                    'absences:failure',
                )
            )

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
    return render(
        request,
        'absences/details.html',
        {
            'ticket': ticket,
        },
    )


def update(request, *args, **kwargs):
    """ Update a ticket. """
    ticket = get_object_or_404(Ticket, pk=kwargs['pk'])
    return render(
        request,
        'absences/form.html',
        {
            'ticket': ticket,
        },
    )


def delete(request, *args, **kwargs):
    """ Delete a ticket. """
    ticket = get_object_or_404(Ticket, pk=kwargs['pk'])
    return render(
        request,
        'absences/delete.html',
        {
            'ticket': ticket,
        },
    )


def send_email(data, monks, mandatory_recipients, additional_recipients):
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
    subject = 'AVIS D\'ABSENCE'
    body = write_body(data, monks)
    body += '\n\n{}'.format(''.join(['-'] * 72))
    body += '\nCe message vous a été envoyé depuis http://python.asj.com:8006/absences.'
    body += '\n{}'.format(''.join(['-'] * 72))
    return send_mail(
        subject,
        body,
        'noreply@python.asj.com',
        recipients_emails,
        fail_silently=False,
    )


def write_body(data, monks):
    """ Write the body of the mail. """
    body = ''
    # Monks
    body += 'Les moines suivants vont s\'absenter :\n{}'.format(monks)

    # Destination:
    body += '\n\nDestination : {}' \
        .format(data['destination']) if data['destination'] else ''

    # Go:
    body += '\n\nDÉPART : {}' \
        .format(data['go_date'])
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
    body += '\n\nRETOUR : {}' \
        .format(data['back_date'])
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
