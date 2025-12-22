""" apps/barcode/views.py """

import os

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
        "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o /home/vincent/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/barcode.svg; \
        convert /home/vincent/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/barcode.svg -transparent '#FFFFFF' -trim /home/vincent/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/barcode.png; \
        rm /home/vincent/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/*.svg; \
        cp /home/vincent/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/barcode.png /home/vincent/Sites/abbaye/abbaye/media/barcode/barcode.png"
        .format(code))

    return JsonResponse(
        {
            'status': 'ready',
        },
    )


def create_qrcode(request, **kwargs):
    """ Create the image of the QR code. """
    code = kwargs['qrcode']

    os.system(
        "qrencode -o /home/vincent/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/qrcode.png '{0}'; \
        cp /home/vincent/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/qrcode.png /home/vincent/Sites/abbaye/abbaye/media/barcode/qrcode.png"
        .format(code))

    return JsonResponse(
        {
            'status': 'ready',
        },
    )
