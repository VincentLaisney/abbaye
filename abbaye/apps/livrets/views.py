""" apps/livrets/views.py """

import os
import datetime
from pathlib import Path

from django.http import JsonResponse
from django.shortcuts import render

from modules.dates import get_first_sunday_of_advent, get_easter


def home(request):
    """ Home page of Livrets. """
    return render(
        request,
        'livrets/home.html',
        {},
    )


def pdf(request):
    """ Create the PDF of the booklet. """
    data = request.GET
    start = data['start'].split('/')
    start = datetime.date(int(start[2]), int(start[1]), int(start[0]))
    for i in range(5):
        date = start + datetime.timedelta(days=i)
        print(date, get_tempo(date))

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


def get_tempo(date):
    """ Return the tempo of the given date. """
    first_sunday_of_advent = get_first_sunday_of_advent(date.year)
    liturgical_year = \
        date.year if date < first_sunday_of_advent\
        else (date.year + 1)
    first_sunday_of_advent = get_first_sunday_of_advent(liturgical_year - 1)
    christmas = datetime.date(liturgical_year - 1, 12, 25)
    if christmas.weekday() == 6:
        holy_family = datetime.date(liturgical_year - 1, 12, 30)
        baptism_of_christ = datetime.date(liturgical_year, 1, 7)
    else:
        holy_family = christmas + \
            datetime.timedelta(days=(6 - christmas.weekday()))
        baptism_of_christ = \
            holy_family + datetime.timedelta(days=14) if christmas.weekday() != 0 \
            else datetime.date(liturgical_year, 1, 7)
    easter = get_easter(liturgical_year)
    ash = easter - datetime.timedelta(days=46)
    pentecost = easter + datetime.timedelta(days=49)
    first_sunday_of_next_advent = get_first_sunday_of_advent(liturgical_year)
    christ_king = first_sunday_of_next_advent - datetime.timedelta(days=7)
    if date >= first_sunday_of_advent and date < christmas:
        tempo = "adv"
    elif date >= christmas and date < baptism_of_christ:
        tempo = "noel"
    elif date >= baptism_of_christ and date < ash:
        tempo = "pa_before_ash"
    elif date >= ash and date < easter:
        tempo = "lent"
    elif date >= easter and date <= pentecost:
        tempo = "tp"
    elif date >= pentecost and date < first_sunday_of_next_advent:
        tempo = "pa_after_pentecost"
    return(tempo)
