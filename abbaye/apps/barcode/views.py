""" apps/barcode/views.py """

import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    """ Home page. """
    return render(
        request,
        'barcode/home.html',
        {},
    )


def create_barcode(request, **kwargs):
    """ Create the image of the barcode. """
    code = kwargs['barcode']

    os.system(
        "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o {1}/apps/barcode/static/barcode/img/barcode.svg; \
        convert {1}/apps/barcode/static/barcode/img/barcode.svg -transparent '#FFFFFF' -trim {1}/apps/barcode/static/barcode/img/barcode.png; \
        rm {1}/apps/barcode/static/barcode/img/*.svg; \
        cp {1}/apps/barcode/static/barcode/img/barcode.png {1}/media/barcode/barcode.png"
        .format(code, settings.BASE_DIR))

    return JsonResponse(
        {
            'status': 'ready',
        },
    )


def create_qrcode(request, **kwargs):
    """ Create the image of the QR code. """
    code = kwargs['qrcode']

    os.system(
        "qrencode -o {1}/apps/barcode/static/barcode/img/qrcode.png '{0}'; \
        cp {1}/apps/barcode/static/barcode/img/qrcode.png {1}/media/barcode/qrcode.png"
        .format(code, settings.BASE_DIR))

    return JsonResponse(
        {
            'status': 'ready',
        },
    )
