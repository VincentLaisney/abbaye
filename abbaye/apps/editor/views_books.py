""" apps/editor/views_books.py """

import os

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .forms import BookForm, ChargeForm
from .models import Charge, Product


def books_list(request):
    """ List of books. """
    books = Product.objects.filter(
        category='book').order_by('ref_tm', 'ean', 'title')
    return render(
        request,
        'editor/books/list.html',
        {
            'books': books
        }
    )


@group_required('Editor')
def book_create(request):
    """ Create a book. """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return HttpResponseRedirect(
                reverse(
                    'editor:book_details',
                    kwargs={
                        'pk': book.pk,
                    }
                )
            )

    else:
        form = BookForm()

    return render(
        request,
        'editor/books/form.html',
        {
            'form': form,
        }
    )


def book_details(request, **kwargs):
    """ Details of a book. """
    book = get_object_or_404(Product, pk=kwargs['pk'])

    # Charges:
    charges = Charge.objects.filter(product=book)
    total_charges = 0
    for index, charge in enumerate(charges):
        total_charges += charge.amount
    cost = (total_charges / book.circulation) if book.circulation else 0
    theorical_price = (cost * book.coefficient) if book.coefficient else 0

    # Barcode:
    if book.ean:
        if not os.path.exists('{}.png'.format(book.ean)):
            # Create the png:
            os.system(
                "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o /home/frromain/Sites/editor/editor/static/img/barcodes/barcode.svg; \
                convert /home/frromain/Sites/editor/editor/static/img/barcodes/barcode.svg -transparent '#FFFFFF' -trim /home/frromain/Sites/editor/editor/static/img/barcodes/{0}.png; \
                rm /home/frromain/Sites/editor/editor/static/img/barcodes/*.svg; \
                cp /home/frromain/Sites/editor/editor/static/img/barcodes/{0}.png /home/frromain/Sites/editor/editor/static_files/img/barcodes/{0}.png"
                .format(book.ean)
            )

    return render(
        request,
        'editor/books/details.html',
        {
            'book': book,
            'charges': charges,
            'total_charges': total_charges,
            'cost': '{:.2f}'.format(cost),
            'theorical_price': '{:.2f}'.format(theorical_price),
            'visual_path': '/img/visuals/{}.jpg'.format(book.ref_tm),
            'barcode_path': '/img/barcodes/{}.png'.format(book.ean),
        },
    )


@group_required('Editor')
def book_update(request, **kwargs):
    """ Update a book. """
    book = Product.objects.get(pk=kwargs['pk'])
    charges_inline_formset = forms.inlineformset_factory(
        Product,
        Charge,
        fields=('name', 'amount'),
        form=ChargeForm,
        can_delete=True,
        extra=1,
    )

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        charges_formset = charges_inline_formset(
            request.POST,
            instance=book,
        )
        if form.is_valid() and charges_formset.is_valid():
            form.save()
            Charge.objects.filter(product=book).delete()
            for form_charge in charges_formset:
                print(form_charge.cleaned_data)
                if form_charge.cleaned_data.get('name') \
                        and form_charge.cleaned_data.get('amount') \
                        and not form_charge.cleaned_data.get('DELETE'):
                    Charge.objects.create(
                        product=book,
                        name=form_charge.cleaned_data.get('name'),
                        amount=form_charge.cleaned_data.get('amount'),
                    )

            return HttpResponseRedirect(
                reverse(
                    'editor:book_details',
                    kwargs={
                        'pk': book.pk,
                    }
                )
            )

    else:
        form = BookForm(instance=book)
        charges_formset = charges_inline_formset(
            instance=book
        )

    return render(
        request,
        'editor/books/form.html',
        {
            'form': form,
            'book': book,
            'charges_formset': charges_formset,
        }
    )


@group_required('Editor')
def book_delete(request, **kwargs):
    """ Delete a book. """
    book = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'editor/books/delete.html', {'book': book})
