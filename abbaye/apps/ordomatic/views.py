""" apps/ordomatic/views.py """

import os
from pathlib import Path
from datetime import date

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    """ Home page of Ordomatic. """
    year = date.today().year
    return render(
        request,
        'ordomatic/home.html',
        {
            'year': year,
        },
    )


def pdf(request, *args, **kwargs):
    """ Create the PDF of the ordo. """
    year = kwargs['year']
    write_pdf(year)
    command = "cd {base_dir}/apps/ordomatic/tex; lualatex --shell-escape ordo.tex; cp ordo.pdf {media_dir}/ordomatic/{year}.pdf".format(
        base_dir=settings.BASE_DIR,
        media_dir=settings.MEDIA_ROOT,
        year=year,
    )
    os.system(command)

    return (
        JsonResponse(
            {
                'status': 'ready',
            },
        )
    )


def write_pdf(year):
    """ Write the PDF of the Ordo according to the year. """
    tex = ''
    tex = '\\input{config.tex}\\par\n\n'
    tex += '\\begin{document}\\par\n'
    tex += 'Ordo {} !\\par\n'.format(year)
    tex += '\\end{document}\n'

    with open(os.path.join(Path(__file__).resolve().parent, 'tex/ordo.tex'), 'w') as tex_file:
        tex_file.write(tex)
