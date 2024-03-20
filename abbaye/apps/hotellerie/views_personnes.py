""" apps/personnes/views_personnes.py """

import re
from dal import autocomplete

from django import forms
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .forms import AdresseForm, MailForm, PersonneForm, TelephoneForm
from .models import Adresse, Mail, Personne, Telephone


@group_required('Hôtellerie')
def list(request):
    """ List of Personnes. """

    personnes = Personne.objects.all().order_by('nom', 'prenom')

    return render(
        request,
        'hotellerie/personnes/list.html',
        {
            'personnes': personnes,
        }
    )


@group_required('Hôtellerie')
def create(request):
    """ Create a Personne. """
    mails_inline_formset = forms.inlineformset_factory(
        Personne,
        Mail,
        fields=('mail',),
        form=MailForm,
        can_delete=True,
        extra=1,
    )
    tels_inline_formset = forms.inlineformset_factory(
        Personne,
        Telephone,
        fields=('num_tel',),
        form=TelephoneForm,
        can_delete=True,
        extra=1,
    )
    adresses_inline_formset = forms.inlineformset_factory(
        Personne,
        Adresse,
        fields=('rue', 'code_postal', 'ville', 'pays',),
        form=AdresseForm,
        can_delete=True,
        extra=1,
    )

    if request.method == 'POST':
        form = PersonneForm(request.POST)
        mails_formset = mails_inline_formset(request.POST)
        tels_formset = tels_inline_formset(request.POST)
        adresses_formset = adresses_inline_formset(request.POST)

        if form.is_valid() \
                and mails_formset.is_valid() \
                and tels_formset.is_valid() \
                and adresses_formset.is_valid():
            personne = form.save()

            for form_mail in mails_formset:
                if form_mail.cleaned_data.get('mail') \
                        and not form_mail.cleaned_data.get('DELETE'):
                    Mail.objects.create(
                        personne=personne,
                        mail=form_mail.cleaned_data.get('mail'),
                    )

            for form_tel in tels_formset:
                if form_tel.cleaned_data.get('num_tel') \
                        and not form_tel.cleaned_data.get('DELETE'):
                    Telephone.objects.create(
                        personne=personne,
                        num_tel=form_tel.cleaned_data.get('num_tel'),
                    )

            for form_adresse in adresses_formset:
                if form_adresse.cleaned_data.get('rue') \
                        or form_adresse.cleaned_data.get('code_postal')\
                        or form_adresse.cleaned_data.get('ville') \
                        or form_adresse.cleaned_data.get('pays'):
                    if not form_adresse.cleaned_data.get('DELETE'):
                        Adresse.objects.create(
                            personne=personne,
                            rue=form_adresse.cleaned_data.get('rue'),
                            code_postal=form_adresse.cleaned_data.get(
                                'code_postal'),
                            ville=form_adresse.cleaned_data.get('ville'),
                            pays=form_adresse.cleaned_data.get('pays'),
                        )

            return HttpResponseRedirect(reverse(
                'hotellerie:personnes_details',
                kwargs={'pk': personne.id}
            ))

    else:
        form = PersonneForm()
        mails_formset = mails_inline_formset()
        tels_formset = tels_inline_formset()
        adresses_formset = adresses_inline_formset()

    return render(request, 'hotellerie/personnes/form.html', {
        'form': form,
        'mails_formset': mails_formset,
        'tels_formset': tels_formset,
        'adresses_formset': adresses_formset,
    })


@group_required('Hôtellerie')
def details(request, **kwargs):
    """ Details of a Personne. """
    personne = get_object_or_404(Personne, pk=kwargs['pk'])
    return render(request, 'hotellerie/personnes/details.html', {
        'personne': personne,
        'mails': Mail.objects.filter(personne=personne),
        'tels': Telephone.objects.filter(personne=personne),
        'adresses': Adresse.objects.filter(personne=personne),
    })


@group_required('Hôtellerie')
def update(request, **kwargs):
    """ Update a Personne. """
    personne = get_object_or_404(Personne, pk=kwargs['pk'])
    first_letter = personne.nom[0] if personne.nom else '-'
    mails_inline_formset = forms.inlineformset_factory(
        Personne,
        Mail,
        fields=('mail',),
        form=MailForm,
        can_delete=True,
        extra=1,
    )
    tels_inline_formset = forms.inlineformset_factory(
        Personne,
        Telephone,
        fields=('num_tel',),
        form=TelephoneForm,
        can_delete=True,
        extra=1,
    )
    adresses_inline_formset = forms.inlineformset_factory(
        Personne,
        Adresse,
        fields=('rue', 'code_postal', 'ville', 'pays',),
        form=AdresseForm,
        can_delete=True,
        extra=1,
    )

    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=personne)
        mails_formset = mails_inline_formset(
            request.POST, instance=personne
        )
        tels_formset = tels_inline_formset(
            request.POST, instance=personne
        )
        adresses_formset = adresses_inline_formset(
            request.POST, instance=personne
        )

        if form.is_valid() \
                and mails_formset.is_valid() \
                and tels_formset.is_valid() \
                and adresses_formset.is_valid():
            form.save()
            Mail.objects.filter(personne=personne).delete()
            Telephone.objects.filter(personne=personne).delete()
            Adresse.objects.filter(personne=personne).delete()

            for form_mail in mails_formset:
                if form_mail.cleaned_data.get('mail') \
                        and not form_mail.cleaned_data.get('DELETE'):
                    Mail.objects.create(
                        personne=personne,
                        mail=form_mail.cleaned_data.get('mail'),
                    )

            for form_tel in tels_formset:
                if form_tel.cleaned_data.get('num_tel') \
                        and not form_tel.cleaned_data.get('DELETE'):
                    Telephone.objects.create(
                        personne=personne,
                        num_tel=form_tel.cleaned_data.get('num_tel'),
                    )

            for form_adresse in adresses_formset:
                if form_adresse.cleaned_data.get('rue') \
                        or form_adresse.cleaned_data.get('code_postal')\
                        or form_adresse.cleaned_data.get('ville') \
                        or form_adresse.cleaned_data.get('pays'):
                    if not form_adresse.cleaned_data.get('DELETE'):
                        Adresse.objects.create(
                            personne=personne,
                            rue=form_adresse.cleaned_data.get('rue'),
                            code_postal=form_adresse.cleaned_data.get(
                                'code_postal'),
                            ville=form_adresse.cleaned_data.get('ville'),
                            pays=form_adresse.cleaned_data.get('pays'),
                        )

            return HttpResponseRedirect(reverse(
                'hotellerie:personnes_details',
                kwargs={'pk': personne.id}
            ))

    else:
        form = PersonneForm(
            instance=personne,
        )
        mails_formset = mails_inline_formset(
            instance=personne
        )
        tels_formset = tels_inline_formset(
            instance=personne
        )
        adresses_formset = adresses_inline_formset(
            instance=personne
        )

    return render(request, 'hotellerie/personnes/form.html', {
        'form': form,
        'personne': personne,
        'first_letter': first_letter,
        'mails_formset': mails_formset,
        'tels_formset': tels_formset,
        'adresses_formset': adresses_formset,
    })


@group_required('Hôtellerie')
def delete(request, **kwargs):
    """ Delete a Personne. """
    personne = get_object_or_404(Personne, pk=kwargs['pk'])
    first_letter = personne.nom[0] if personne.nom else '-'

    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=personne)
        personne.delete()
        return HttpResponseRedirect(reverse('hotellerie:personnes_list', args=first_letter))

    else:
        form = PersonneForm(instance=personne)

    return render(request, 'hotellerie/personnes/delete.html', {
        'form': form,
        'personne': personne,
        'first_letter': first_letter
    })


@group_required('Hôtellerie')
def get_pere_suiveur(request):
    """ Returns the pere_suiveur of a personne and checks if this pere_suiveur has an email. """
    personne = Personne.objects.get(pk=request.GET['personne'])
    pere_suiveur = personne.pere_suiveur if personne.pere_suiveur else None
    if not pere_suiveur:
        return JsonResponse({})
    pere_suiveur_str = pere_suiveur.__str__()
    has_mail = pere_suiveur.mail_personne.count() > 0
    return JsonResponse({
        'pere_suiveur': pere_suiveur_str,
        'has_mail': has_mail
    })


class PersonneAutocompleteHotesView(autocomplete.Select2QuerySetView):
    """ Return a set of Hotes according to the user search value. """

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Personne.objects.none()

        personnes = Personne.objects.filter(moine_flav=False)
        if self.q:
            personnes = (personnes.filter(nom__icontains=self.q) |
                         personnes.filter(prenom__icontains=self.q))
        return personnes.order_by('nom', 'prenom', 'last_modified')


class PersonneAutocompleteMonksView(autocomplete.Select2QuerySetView):
    """ Return a set of Monks according to the user search value. """

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Personne.objects.none()

        personnes = Personne.objects.filter(moine_flav=True)
        if self.q:
            personnes = (personnes.filter(nom__icontains=self.q) |
                         personnes.filter(prenom__icontains=self.q))
        return personnes.order_by('nom', 'prenom', 'last_modified')
