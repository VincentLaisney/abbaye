""" apps/livrets/views.py """

import os
from pathlib import Path

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    """ Home page of Livrets. """
    return render(
        request,
        'livrets/home.html',
        {},
    )


def pdf(request):
    """ Return OK when PDF is created. """
    data = request.GET

    tex = ''
    tex = '\\input{config.tex}\n\n'
    tex += '\\begin{document}\n\n'
    tex += '\\setlength{\\columnseprule}{0.5pt}\n'
    tex += '\\colseprulecolor{rougeliturgique}\n\n'
    tex += '\\thispagestyle{empty}\n\n'
    tex += '\\begin{center}\n'
    tex += '+\\par\n'
    tex += 'PAX\\par\n'
    tex += '\\vspace{.5cm}\n'
    tex += '\\TitreB{Abbaye Saint-Joseph de Clairval}\n'
    tex += '\\end{center}\n\n'
    tex += '\\TitreA{Messe conventuelle}\n\n'
    for i in range(5):
        tex += data['date_'+str(i+1)]+'\n\n'
        tex += data['in_'+str(i+1)]+'\n\n'
    tex += '\\end{document}\n\n'

    with open(os.path.join(Path(__file__).resolve().parent, 'tex/livret.tex'), 'w') as tex_file:
        tex_file.write(tex)
    return JsonResponse(
        {'back': 'OK'},
    )
