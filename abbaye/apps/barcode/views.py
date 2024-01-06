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


def create(request, **kwargs):
    """ Create the image of the barcode (if needed). """
    code = kwargs['barcode']
    path = "/home/frromain/Sites/abbaye/abbaye/statics/barcode/img/archives/{0}.png".format(
        code)

    if not os.path.exists(path):
        os.system(
            "barcode -b {0} -e 'ean13' -u mm -g 100x50 -S -o /home/frromain/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/barcode.svg; \
            convert /home/frromain/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/barcode.svg -transparent '#FFFFFF' -trim /home/frromain/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/archives/{0}.png; \
            rm /home/frromain/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/*.svg; \
            cp /home/frromain/Sites/abbaye/abbaye/apps/barcode/static/barcode/img/archives/{0}.png /home/frromain/Sites/abbaye/abbaye/statics/barcode/img/archives/{0}.png"
            .format(code))

    return JsonResponse(
        {
            'status': 'ready',
        },
    )
