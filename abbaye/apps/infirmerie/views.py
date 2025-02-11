""" apps/infirmerie/views.py """

import datetime
import io

from reportlab.lib.pagesizes import A6
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from dal import autocomplete

from .models import Billet, Speciality, Toubib
from .forms import BilletForm, SpecialityForm, ToubibForm


def home(request):
    """ Home page of Infirmerie. """
    return render(
        request,
        'infirmerie/home.html',
        {},
    )


class ToubibListView(LoginRequiredMixin, ListView):
    """ List of Toubibs. """
    template_name = 'toubibs/list.html'
    paginate_by = 20

    def get_queryset(self):
        if 'search' in self.kwargs:
            search = self.kwargs['search']
            queryset = (Toubib.objects.filter(nom__icontains=search)
                        | Toubib.objects.filter(specialite__icontains=search))
        else:
            queryset = Toubib.objects
        return queryset.order_by('nom', 'prenom')


@login_required
def toubibs_repertoire(request, **kwargs):
    """ Toubibs as repertoire. """
    toubibs = Toubib.objects.filter(
        nom__startswith=kwargs['letter']).order_by('nom', 'prenom')
    return render(
        request,
        'toubibs/repertoire.html',
        {
            'letters': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-'],
            'toubibs': toubibs,
            'current': kwargs['letter'],
        }
    )


class ToubibCreateView(LoginRequiredMixin, CreateView):
    """ Create Toubib. """
    model = Toubib
    form_class = ToubibForm
    template_name = 'toubibs/form.html'
    success_url = reverse_lazy('toubibs:list', args=[1])


class ToubibDetailView(LoginRequiredMixin, DetailView):
    """ Detail of Toubib. """
    fields = ('__all__')
    model = Toubib
    template_name = 'toubibs/detail.html'


class ToubibUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Toubib. """
    model = Toubib
    form_class = ToubibForm
    template_name = 'toubibs/form.html'
    success_url = reverse_lazy('toubibs:list', args=[1])


class ToubibDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete toubib. """
    model = Toubib
    success_url = reverse_lazy('toubibs:list', args=[1])
    template_name = "toubibs/delete.html"


class ToubibAutocompleteView(autocomplete.Select2QuerySetView):
    """ Return a set of Toubibs according to the user search value. """

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Toubib.objects.none()

        toubibs = Toubib.objects.all()
        if self.q:
            toubibs = toubibs.filter(nom__istartswith=self.q)
        return toubibs


@login_required
def specialities_list(request):
    """ List of specialities. """
    specialities = Speciality.objects.all().order_by('speciality')
    return render(
        request,
        'specialities/list.html',
        {
            'specialities': specialities
        }
    )


@login_required
def specialities_create(request):
    """ Create a speciality. """
    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('toubibs:specialities_list'))

    else:
        form = SpecialityForm()

    return render(
        request,
        'specialities/form.html',
        {'form': form}
    )


@login_required
def specialities_update(request, **kwargs):
    """ Update a speciality. """
    spe = get_object_or_404(Speciality, pk=kwargs['pk'])

    if request.method == 'POST':
        form = SpecialityForm(request.POST, instance=spe)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('toubibs:specialities_list'))

    else:
        form = SpecialityForm(instance=spe)

    return render(
        request,
        'specialities/form.html',
        {
            'form': form,
            'spe': spe,
        }
    )


@login_required
def specialities_delete(request, **kwargs):
    """ Delete a speciality. """
    spe = get_object_or_404(Speciality, pk=kwargs['pk'])

    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        spe.delete()
        return HttpResponseRedirect(reverse('toubibs:specialities_list'))

    else:
        form = SpecialityForm()

    return render(request, 'specialities/delete.html', {
        'form': form,
        'spe': spe,
    })


class HomeView(RedirectView):
    """ Home view: redirect to agenda. """

    def get_redirect_url(self, *args, **kwargs):
        today = datetime.date.today()
        day = today.strftime('%d')
        month = today.strftime('%m')
        year = today.strftime('%Y')
        return reverse('billets:agenda', kwargs={'day': day, 'month': month, 'year': year})


class AgendaView(LoginRequiredMixin, ListView):
    """ Agenda (main page of the app). """
    template_name = "billets/agenda.html"
    queryset = Billet.objects.all().order_by('-when')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        date_today = datetime.date.today()
        context['today'] = {'day': date_today.strftime(
            '%d'), 'month': date_today.strftime('%m'), 'year': date_today.strftime('%Y')}

        # Date that has been required in **kwargs:
        display_date = datetime.datetime(
            int(self.kwargs['year']), int(self.kwargs['month']), int(self.kwargs['day']))

        # Initial date of the week containing the required date:
        initial_date = display_date - \
            datetime.timedelta(days=(display_date.weekday() + 1)
                               if display_date.weekday() != 6 else 0)

        # Construct the list of days with all their data:
        days = {}
        for i in range(7):
            date = initial_date + datetime.timedelta(days=i)
            date_human = datetime.date(date.year, date.month, date.day)
            days[date_human] = {}
            days[date_human]['billets'] = Billet.objects.filter(when__gt=date).filter(
                when__lt=(date + datetime.timedelta(days=1)))
            days[date_human]['current'] = (date_human == datetime.date.today())
        context['days'] = days

        return context


@login_required
def billets_list_view(request, page=0):
    """ Billets as list. """
    billets = Billet.objects.all().order_by('when', 'titre')
    paginator = Paginator(billets, 20)
    if page == 0:
        page = paginator.num_pages
    page_obj = paginator.page(page)
    billets = page_obj.object_list
    return render(
        request,
        'billets/list.html',
        {
            'is_paginated': True,
            'billets': billets,
            'paginator': paginator,
            'page_obj': page_obj,
        }
    )


class BilletCreateView(LoginRequiredMixin, CreateView):
    """ Create Billet. """
    model = Billet
    form_class = BilletForm
    template_name = 'billets/form.html'
    success_url = reverse_lazy('billets:home')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class BilletDetailView(LoginRequiredMixin, DetailView):
    """ Detail of Billet. """
    fields = ('__all__')
    model = Billet
    template_name = 'billets/detail.html'


class BilletUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Billet. """
    model = Billet
    form_class = BilletForm
    template_name = 'billets/form.html'
    success_url = reverse_lazy('billets:home')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class BilletDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete billet. """
    model = Billet
    success_url = reverse_lazy('billets:home')
    template_name = "billets/delete.html"


class BilletPDFView(LoginRequiredMixin, View):
    """ Display billet as pdf. """

    def get(self, request, *args, **kwargs):
        """ Return pdf of billet in browser. """
        billet = Billet.objects.get(pk=self.kwargs['pk'])
        buffer = io.BytesIO()

        # Settings:
        width, height = A6
        pdf = canvas.Canvas(buffer, pagesize=A6, bottomup=0)
        pdf.setFont("Helvetica", 10)
        pdf.saveState()
        pdf.setLineWidth(0.2)

        # Header:
        pdf.drawCentredString(width/2.0, 8 * mm, '+')
        pdf.drawCentredString(width/2.0, 13 * mm, 'PAX')
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawCentredString(width/2.0, 55, 'Rendez-vous médical')
        if billet.where == 'Porterie':
            where = ' (à la porterie)'
        elif billet.where == 'Infirmerie':
            where = ' (à l\'infirmerie)'
        else:
            where = ''
        pdf.drawCentredString(
            width/2.0, 70,
            '{}{}'.format(
                billet.date_time(),
                where
            )
        )
        pdf.restoreState()
        pdf.saveState()

        # Médecin :
        add = 0
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(10 * mm, 33 * mm, 'Médecin')
        pdf.roundRect(7 * mm, 35 * mm, width - 2 * 7 * mm, 30 * mm, 3 * mm)
        toubib = billet.toubib.__str__()
        toubib += (' (Tél. ' + billet.toubib.telephone +
                   ')') if billet.toubib.telephone else ''
        pdf.drawString(10 * mm, 40 * mm, toubib)
        pdf.restoreState()
        if billet.toubib.adresse_1:
            pdf.drawString(15 * mm, 45 * mm, billet.toubib.adresse_1)
        if billet.toubib.adresse_2:
            pdf.drawString(15 * mm, 50 * mm, billet.toubib.adresse_2)
            add += 15
        if billet.toubib.adresse_3:
            pdf.drawString(15 * mm, 55 * mm, billet.toubib.adresse_3)
            add += 15
        if billet.toubib.code_postal and billet.toubib.ville:
            pdf.drawString(15 * mm, 50 * mm + add, billet.toubib.code_postal +
                           ' ' + billet.toubib.ville)
        pdf.saveState()

        # Moine :
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(10 * mm, 73 * mm, 'Moine(s) concerné(s)')
        pdf.roundRect(7 * mm, 75 * mm, width - 2 * 7 * mm, 23 * mm, 3 * mm)
        pdf.restoreState()
        pdf.rect(10 * mm, 78 * mm, 2 * mm, 2 * mm)
        pdf.drawString(15 * mm, 80 * mm, billet.moine1.__str__())
        if billet.moine2:
            pdf.rect(10 * mm, 83 * mm, 2 * mm, 2 * mm)
            pdf.drawString(15 * mm, 85 * mm, billet.moine2.__str__())
        if billet.moine3:
            pdf.rect(10 * mm, 88 * mm, 2 * mm, 2 * mm)
            pdf.drawString(15 * mm, 90 * mm, billet.moine3.__str__())
        if billet.moine4:
            pdf.rect(10 * mm, 93 * mm, 2 * mm, 2 * mm)
            pdf.drawString(15 * mm, 95 * mm, billet.moine4.__str__())
        pdf.saveState()

        # Divers (prix, chauffeur, remarques):
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(10 * mm, 106 * mm, 'Remarques')
        pdf.roundRect(7 * mm, 108 * mm, width - 2 * 7 * mm, 35 * mm, 3 * mm)
        pdf.restoreState()
        pdf.setFont("Helvetica", 8)
        # Prix :
        prix = 'Prix :'
        if billet.gratis or billet.prix == 0:
            prix += ' gratis pro Deo'
        elif billet.prix:
            """ Prix avec la partie décimale
            le cas échéant, sinon entier. """
            prix += ' {:.2f} €'.format(billet.prix) \
                if str(billet.prix - int(billet.prix))[1:] != '.0' \
                else ' {:.0f} €'.format(billet.prix)
            prix += ' (facture)' if billet.facture else ''
        else:
            prix += ' ?'
        prix += ' - Apporter la carte vitale' if billet.vitale else ''
        pdf.drawString(10 * mm, 113 * mm, prix)
        # Chauffeur :
        add = 0
        if billet.chauffeur:
            pdf.drawString(10 * mm, 118 * mm, 'Chauffeur : ' +
                           billet.chauffeur.__str__())
            add = 5
        # Remarques :
        if billet.remarque:
            for index, line in enumerate(billet.remarque.splitlines()):
                remarque = pdf.beginText(
                    10 * mm, (118 + add + (5 * index)) * mm)
                remarque.textLine(line)
                pdf.drawText(remarque)

        pdf.showPage()
        pdf.save()
        buffer.seek(0)
        return FileResponse(buffer, filename='billet.pdf')
