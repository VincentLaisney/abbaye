""" apps/editor/views_images.py """

import os

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.main.decorators import group_required

from .forms import ImageForm
from .models import Product


def images_list(request):
    """ List of images. """
    images = Product.objects.filter(category='image').order_by(
        'ref_tm', 'ean', 'recto_img', 'verso_img')
    return render(
        request,
        'editor/images/list.html',
        {
            'images': images
        }
    )


@group_required('Editor')
def image_create(request):
    """ Create an image. """
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save()
            return HttpResponseRedirect(
                reverse(
                    'editor:image_details',
                    kwargs={
                        'pk': image.pk,
                    }
                )
            )

    else:
        form = ImageForm()

    return render(
        request,
        'editor/images/form.html',
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
                "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/barcode.svg; \
                convert /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/barcode.svg -transparent '#FFFFFF' -trim /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/{0}.png; \
                rm /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/*.svg; \
                cp /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor/img/barcodes/{0}.png /home/frromain/Sites/abbaye/abbaye/apps/editor/static/editor_files/img/barcodes/{0}.png"
                .format(image.ean)
            )

    return render(
        request,
        'editor/images/details.html',
        {
            'image': image,
            'visual_path': '/editor/img/visuals/{}.jpg'.format(image.ref_tm),
            'barcode_path': '/editor/img/barcodes/{}.png'.format(image.ean),
        },
    )


@group_required('Editor')
def image_update(request, **kwargs):
    """ Update an image. """
    image = Product.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        form = ImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'editor:image_details',
                    kwargs={
                        'pk': image.pk,
                    }
                )
            )

    else:
        form = ImageForm(instance=image)

    return render(
        request,
        'editor/images/form.html',
        {
            'form': form,
            'image': image,
        }
    )


@group_required('Editor')
def image_delete(request, **kwargs):
    """ Delete a image. """
    image = Product.objects.get(pk=kwargs['pk'])
    return render(request, 'editor/images/delete.html', {'image': image})
