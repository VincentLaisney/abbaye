""" apps/editor/views_images.py """

import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ImageForm
from .models import Product


def images_list(request):
    """ List of images. """
    images = Product.objects.filter(category='image').order_by(
        'ref_tm', 'ean', 'recto_img', 'verso_img')
    return render(
        request,
        'editorimages/list.html',
        {
            'images': images
        }
    )


@login_required
def image_create(request):
    """ Create an image. """
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save()
            return HttpResponseRedirect(
                reverse(
                    'products:image_details',
                    kwargs={
                        'pk': image.pk,
                    }
                )
            )

    else:
        form = ImageForm()

    return render(
        request,
        'editorimages/form.html',
        {
            'form': form,
        }
    )


def image_details(request, **kwargs):
    """ Details of an image. """
    image = get_object_or_404(Product, pk=kwargs['pk'])

    # Barcode:
    if image.ean:
        if not os.path.exists('{}.png'.format(image.ean)):
            # Create the png:
            os.system(
                "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o static/img/barcodes/barcode.svg; \
                convert static/img/barcodes/barcode.svg -transparent '#FFFFFF' -trim static/img/barcodes/{0}.png; \
                rm static/img/barcodes/*.svg"
                .format(image.ean)
            )

    return render(
        request,
        'editorimages/details.html',
        {
            'image': image,
            'visual_path': '/img/visuals/{}.jpg'.format(image.ref_tm),
            'barcode_path': '/img/barcodes/{}.png'.format(image.ean),
        },
    )


@login_required
def image_update(request, **kwargs):
    """ Update an image. """
    image = Product.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        form = ImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'products:image_details',
                    kwargs={
                        'pk': image.pk,
                    }
                )
            )

    else:
        form = ImageForm(instance=image)

    return render(
        request,
        'editorimages/form.html',
        {
            'form': form,
            'image': image,
        }
    )


@login_required
def image_delete(request, **kwargs):
    """ Delete a image. """
    image = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'editorimages/delete.html', {'image': image})
