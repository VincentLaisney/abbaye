""" apps/livrets/views.py """

from math import ceil, floor
import os
import datetime
from pathlib import Path

from django.http import JsonResponse
from django.shortcuts import render

from modules.dates import get_first_sunday_of_advent, get_easter

from .models import BMV, Day, Preface, Score


def home(request):
    """ Home page of Livrets. """
    return render(
        request,
        'livrets/home.html',
        {},
    )


def pdf(request):
    """ Create the PDF of the booklet. """
    request_get = request.GET
    # print(request_get)
    start = request_get['start'].split('/')
    start = datetime.date(int(start[2]), int(start[1]), int(start[0]))

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
    tex += '\\TitreA{Messe conventuelle}\n'
    for i in range(5):
        date = start + datetime.timedelta(days=i)
        year_cycle = ['A', 'B', 'C'][(date.year - 2020) % 3]
        year_even = 2 if date.year % 2 == 0 else 1
        data = get_data(date)
        print(data)

        # Liturgical day:
        tex += "\n\\section{{{}}}\n".format(
            request_get['date_' + str(i + 1)],
        )
        tex += "\\JourLiturgique{{{}}}{{{}}}\\par\n".format(
            data['title'],
            data['rang'] if data['rang'] else '',
        )

        # Introit:
        grid_in = request_get['in_' + str(i + 1)]
        if grid_in:
            introit = Score.objects.filter(
                type='IN',
            ).filter(
                ref=grid_in
            ).first()
            if introit:
                tex += '\\TitreB{{Antienne d\'Introït~:}}\\Normal{{\\textit{{{}}} (p. {}).}}\\par\n'.format(
                    introit.name,
                    introit.page,
                )
            else:
                tex += '\\TitreB{Antienne d\'Introït~:}\\par\\par\n'
                tex += '\\PartocheWithTraduction{{GR/introit/{}}}\\par\n'.format(
                    grid_in,
                )

        # Ouverture:
        tex += "\\TitreB{Ouverture de la célébration~:}\\Normal{p. 7.}\\par\n"

        # Tierce:
        tierce_antiphon = \
            data['tierce'] if data['tierce'] \
            else [
                'adjuva_me',
                'clamavi',
                'servite_domino',
                'exsurge_domine',
                'inclina_domine',
                'vivit_dominus',
                'alleluia_dim_per_annum',
            ][date.weekday()]
        tierce_page = ['4', '6', '9', '12', '15', '17', '2'][date.weekday()]
        tex += "\\TierceMG{{{}}}{{{}}}\\par\n".format(
            tierce_antiphon,
            tierce_page,
        )

        # Prayer Collecte:
        if data['prayers_mg']:
            tex += "\\TitreB{{Oraison~:}}\\Normal{{p. {}}}\\par\n".format(
                data['prayers_mg'].split('/')[0]
            )
        else:
            tex += "\\Oraison{{Oraison}}{{1}}{{{}}}\\par\n".format(
                data['ref'],
            )

        # First reading:
        tex += '\\Lecture{{Première lecture}}{{{}'.format(
            data['readings'],
        )
        if data['readings_cycle'] == 3:
            tex += "_{}_1}}\\par\n".format(
                year_cycle,
            )
        elif data['readings_cycle'] == 2:
            tex += "_1_{}}}\\par\n".format(
                year_even,
            )
        elif data['readings_cycle'] == 1:
            tex += "_1}}\\par\n"

        # Graduel:
        grid_gr = request_get['gr_' + str(i + 1)]
        if grid_gr:
            graduel = Score.objects.filter(
                type='GR',
            ).filter(
                ref=grid_gr
            ).first()
            if graduel:
                tex += '\\TitreB{{Graduel~:}}\\Normal{{\\textit{{{}}} (p. {}).}}\\par\n'.format(
                    graduel.name,
                    graduel.page,
                )
            else:
                tex += '\\TitreB{Graduel~:}\\par\n'
                tex += '\\PartocheWithTraduction{{GR/graduel/{}}}\\par\n'.format(
                    grid_gr,
                )

        # Second reading (if gr) and alleluia:
        grid_al = request_get['al_' + str(i + 1)]
        if grid_al:
            if grid_gr:
                # Second reading:
                tex += '\\Lecture{{Deuxième lecture}}{{{}'.format(
                    data['readings'],
                )
                if data['readings_cycle'] == 3:
                    tex += "_{}_2}}\\par\n".format(
                        year_cycle,
                    )
                elif data['readings_cycle'] == 2:
                    tex += "_2_{}}}\\par\n".format(
                        year_even,
                    )
                elif data['readings_cycle'] == 1:
                    tex += "_2}}\\par\n"

            # Alleluia:
            alleluia = Score.objects.filter(
                type='AL',
            ).filter(
                ref=grid_al
            ).first()
            if alleluia:
                tex += '\\TitreB{{Alléluia~:}}\\Normal{{\\textit{{{}}} (p. {}).}}\n'.format(
                    alleluia.name,
                    alleluia.page,
                )
            else:
                tex += '\\TitreB{Alléluia~:}\\par\n'
                tex += '\\PartocheWithTraduction{{GR/alleluia/{}}}\n'.format(
                    grid_al,
                )

        # Gospel:
        tex += '\\Lecture{{Évangile~:}}{{{}'.format(
            data['readings'],
        )
        if data['readings'].startswith('pa_') and not data['readings'].endswith('_0'):
            tex += "_ev}\n"
        elif data['readings_cycle'] == 3:
            tex += "_{}_ev}}\\par\n".format(
                year_cycle,
            )
        elif data['readings_cycle'] == 2:
            tex += "_ev_{}}}\\par\n".format(
                year_even,
            )
        elif data['readings_cycle'] == 1:
            tex += "_ev}\\par\n"

        # Prayer Super oblata:
        if data['prayers_mg']:
            tex += "\\TitreB{{Prière sur les offrandes~:}}\\Normal{{p. {}}}\\par\n".format(
                data['prayers_mg'].split('/')[0],
            )
        else:
            tex += "\\Oraison{{Prière sur les offrandes}}{{2}}{{{}}}\\par\n".format(
                data['ref'],
            )

        # Preface:
        preface = Preface.objects.get(pk=data['preface_id'])
        if preface.page:
            tex += "\\TitreB{{{}~:}}\\Normal{{p. {}.}}\\par\n".format(
                preface.name,
                preface.page,
            )
        else:
            tex += "\\Preface{{{}}}{{{}}}\\par\n".format(
                preface.name,
                preface.ref,
            )

        # Canon:
        tex += "\\TitreB{Prière eucharistique n. 1}\\Normal{(p. 22).}\\par\n"
        tex += "\\TitreB{Rites de communion~:}\\Normal{p. 41.}\\par\n"

        # Prayer Postcommunion:
        if data['prayers_mg']:
            tex += "\\TitreB{{Prière après la Communion~:}}\\Normal{{p. {}}}\\par\n".format(
                data['prayers_mg'].split('/')[0],
            )
        else:
            tex += "\\Oraison{{Prière après la Communion}}{{3}}{{{}}}\\par\n".format(
                data['ref'],
            )

        # Conclusion:
        tex += "\\TitreB{Conclusion~:}{\\Normal{p. 47.}}\\par\n"

    tex += "\n\\vspace{3cm}\n"
    tex += "\\begin{center}\n"
    tex += "\\makebox[12.35cm][c]{\\textit{Vous pouvez emporter ce livret si vous le souhaitez.}}\n"
    tex += "\\makebox[12.35cm][c]{\\textit{Merci de rendre le Missel Grégorien bleu.}}\n"
    tex += "\\end{center}\n"
    tex += "\n\\newpage\n"
    tex += "\\pagestyle{plain}\n"
    tex += "\\fontsize{11.5}{13}\\selectfont\n"
    tex += "\n"
    tex += "\\begin{center}\n"
    tex += "\\Normal{\\textbf{Communion spirituelle}}\n"
    tex += "\\end{center}\n"
    tex += "Ô Jésus, mon aimable Sauveur, combien je voudrais en ce moment, m’approcher de votre Table sainte, plein de confiance, non en mes propres mérites, mais en votre infinie bonté~! Que je voudrais aller à vous, Source de miséricorde~; être guéri par vous, divin Médecin de mon âme~; chercher en vous mon appui, en vous, Seigneur, qui serez un jour mon Juge, mais qui ne voulez être, maintenant, que mon Sauveur~! Je vous aime, ô Jésus, Agneau divin, innocente Victime, immolée par amour sur la Croix, pour moi et pour le salut du genre humain. Ô mon Dieu, souvenez-vous de votre humble créature, rachetée par votre Sang~! Je me repens de vous avoir offensé, et je désire réparer mes fautes par les efforts que je ferai pour obéir à votre sainte volonté. Ô bon Jésus, qui, par votre grâce tout-puissante, me fortifiez contre les ennemis de mon âme et de mon corps, faites que bientôt, purifié de toute souillure, j’aie le bonheur de vous recevoir dans la Sainte Eucharistie, afin de travailler avec une constante générosité à l’œuvre de mon salut. Ainsi soit-il.\\par\\vspace{0.2cm}\n"
    tex += "\n"
    tex += "\\begin{center}\n"
    tex += "\\Normal{\\textbf{Prières avant la Communion}}\n"
    tex += "\\end{center}\n"
    tex += "\\textbf{Acte de Foi.} – Ô Seigneur Jésus, je crois que vous êtes réellement et substantiellement présent dans la Sainte Hostie, avec votre Corps, votre Sang, votre Âme et votre Divinité. Je le crois fermement parce que vous l’avez dit, vous qui êtes la vérité même. Je crois que dans ce Sacrement, vous, mon Sauveur, vrai Dieu et vrai homme, vous vous donnez à moi, pour me faire vivre plus abondamment de votre vie divine~; je le crois, mais fortifiez et augmentez ma foi.\n"
    tex += "\\textbf{Acte d’humilité.} – Je reconnais, ô mon Dieu, que je suis une humble créature, sortie de vos mains et de plus, un pauvre pécheur, très indigne de vous recevoir, vous qui êtes le Tout-Puissant, l’éternel, le Dieu infiniment saint. Je devrais vous dire, comme votre apôtre Pierre, et avec bien plus de raison que lui: «~éloignez-vous de moi, parce que je suis un pécheur~»; mais souffrez que je répète avec le Centurion~: «~Seigneur, dites seulement une parole, et mon âme sera guérie.~»\n"
    tex += "\\textbf{Acte de contrition.} – Mon Dieu, je déteste toutes les fautes de ma vie~; je les déteste de tout mon cœur, parce qu’elles vous ont offensé, vous, ô mon Dieu, qui êtes si bon. Je vous en supplie, effacez-les par votre sang. Avec l’aide de votre grâce, je prends la résolution de ne plus commettre le péché, et d’en faire une sincère pénitence.\n"
    tex += "\\textbf{Acte de désir et d’amour.} – Ô Seigneur Jésus, le Dieu de mon cœur, mon bonheur et ma force, vous, le Pain vivant, qui descendez du ciel pour être la nourriture de mon âme, j’ai un grand désir de vous recevoir. Je me réjouis à la pensée que vous allez venir habiter en moi. Venez, Seigneur Jésus, venez posséder mon cœur~; qu’il soit à vous pour toujours! Vous qui m’aimez tant, faites que je vous aime de toute mon âme, et par-dessus toutes choses.\n"
    tex += "\\textbf{Recours à la Très Sainte Vierge et aux Saints.} – Sainte Vierge Marie, Mère de Jésus, le Dieu d’amour qui va s’unir à mon âme dans la Sainte Eucharistie, obtenez-moi la grâce de le recevoir dignement. Saint Joseph, Saints et Bienheureux, et vous, mon bon Ange gardien, intercédez pour moi.\\par\\vspace{0.2cm}\n"
    tex += "\n"
    tex += "\\begin{center}\n"
    tex += "\\Normal{\\textbf{Prières après la Communion}}\n"
    tex += "\\end{center}\n"
    tex += "\\textbf{Acte de Foi et d’Adoration.} – Ô Jésus, je le crois, c’est vous que je viens de recevoir, vous, mon Dieu, mon Créateur et mon Maître, vous qui, par amour pour moi, avez été, à votre naissance, couché sur la paille de la crèche, vous qui avez voulu mourir pour moi sur la Croix. J’ai été tiré du néant par votre toute-puissance, et vous venez habiter en moi~! Ô mon Dieu, saisi d’un profond respect, je me prosterne devant votre souveraine majesté, je vous adore, et je vous offre mes plus humbles louanges.\n"
    tex += "\\textbf{Acte de Reconnaissance et d’Amour.} – Très doux Jésus, Dieu d’infinie bonté, je vous remercie de tout mon cœur, pour la grâce insigne que vous venez de me faire. Que vous rendrai-je pour un tel bienfait~? Je voudrais vous aimer, autant que vous êtes aimable, et vous servir, autant que vous méritez de l’être. Ô Dieu, qui êtes tout amour, apprenez-moi à vous aimer, d’une affection véritable et fidèle, et enseignez-moi à faire votre sainte volonté. Je m’offre tout entier à vous: mon corps, afin qu’il soit chaste; mon âme, afin qu’elle soit pure de tout péché; mon cœur, afin qu’il ne cesse de vous aimer. Vous vous êtes donné à moi, je me donne à vous pour toujours.\n"
    tex += "\\textbf{Acte de Demande.} – Vous êtes en moi, ô Jésus, vous qui avez dit: «~Demandez et vous recevrez~». Vous y êtes, rempli de bonté pour moi, les mains pleines de grâces~; daignez les répandre sur mon âme, qui en a tant besoin. Ôtez de mon cœur tout ce qui vous déplaît, mettez-y tout ce qui peut le rendre agréable à vos yeux. Appliquez-moi les mérites de votre vie et de votre mort, unissez-moi à vous, vivez en moi, faites que je vive par vous et pour vous. Accordez aussi, Dieu infiniment bon, les mêmes grâces à toutes les personnes pour lesquelles j’ai le devoir de prier, ou à qui j’ai promis particulièrement de le faire. – Cœur miséricordieux de Jésus, ayez pitié des pauvres âmes du purgatoire, et donnez-leur le repos éternel.\n"

    tex += '\n\\end{document}\n\n'

    with open(os.path.join(Path(__file__).resolve().parent, 'tex/livret.tex'), 'w') as tex_file:
        tex_file.write(tex)
    return JsonResponse(
        {'back': 'OK'},
    )


def get_data(date):
    """ Return the data of the given date. """
    # tempo_ref:
    weekday = (date.weekday() + 1) if date.weekday() != 6 else 0
    first_sunday_of_advent = get_first_sunday_of_advent(date.year)
    liturgical_year = date.year if date < first_sunday_of_advent\
        else (date.year + 1)
    first_sunday_of_advent = get_first_sunday_of_advent(liturgical_year - 1)
    christmas = datetime.date(liturgical_year - 1, 12, 25)
    if christmas.weekday() == 6:
        holy_family = datetime.date(liturgical_year - 1, 12, 30)
        baptism_of_christ = datetime.date(liturgical_year, 1, 7)
    else:
        holy_family = christmas + \
            datetime.timedelta(days=(6 - christmas.weekday()))
        baptism_of_christ = holy_family + datetime.timedelta(days=14) if christmas.weekday() != 0 \
            else datetime.date(liturgical_year, 1, 7)
    easter = get_easter(liturgical_year)
    ash = easter - datetime.timedelta(days=46)
    pentecost = easter + datetime.timedelta(days=49)
    first_sunday_of_next_advent = get_first_sunday_of_advent(liturgical_year)
    christ_king = first_sunday_of_next_advent - datetime.timedelta(days=7)
    if first_sunday_of_advent <= date < christmas:
        tempo_ref = 'adv'
    elif christmas <= date < baptism_of_christ:
        tempo_ref = 'noel'
    elif baptism_of_christ <= date < ash:
        tempo_ref = 'pa_before_ash'
    elif ash <= date < easter:
        tempo_ref = 'lent'
    elif easter <= date <= pentecost:
        tempo_ref = 'tp'
    elif pentecost <= date < first_sunday_of_next_advent:
        if date == pentecost + datetime.timedelta(days=7):
            tempo_ref = 'trinite'
        elif date == pentecost + datetime.timedelta(days=11):
            tempo_ref = 'fete_dieu'
        elif date == pentecost + datetime.timedelta(days=19):
            tempo_ref = 'sacre_coeur'
        elif date == christ_king:
            tempo_ref = 'christ_roi'
        else:
            days = (first_sunday_of_next_advent - date).days
            week = 35 - floor((days / 7) + 1)
            tempo_ref = 'pa_{}_{}'.format(week, weekday)
    data = Day.objects.filter(ref=tempo_ref).values()[0]
    data['readings'] = tempo_ref

    # Sancto:
    month = date.strftime('%m')
    day = date.day
    sancto_ref = '{}{}'.format(month, day)
    sancto = Day.objects.filter(ref=sancto_ref)
    if sancto:
        sancto_values = sancto.values()[0]
        if sancto_values['precedence'] > data['precedence']:
            data['id'] = sancto_values['id']
            data['ref'] = sancto_values['ref']
            data['title'] = sancto_values['title']
            data['rang'] = sancto_values['rang']
            data['tierce'] = sancto_values['tierce']
            data['prayers_mg'] = sancto_values['prayers_mg']
            data['proper_readings'] = sancto_values['proper_readings']
            data['readings'] = sancto_ref
            data['readings_cycle'] = sancto_values['readings_cycle']
            data['preface_id'] = sancto_values['preface_id']
            data['preface_name_latin'] = sancto_values['preface_name_latin']
            data['preface_name_french'] = sancto_values['preface_name_french']
            data['sequence'] = sancto_values['sequence']

    elif weekday == 6 and data['precedence'] < 30:
        ref_bmv = 'icm' if day < 8 \
            else '{}_{}'.format(
                date.month,
                ceil(date.day / 7),
            )
        bmv = BMV.objects.filter(ref=ref_bmv).values()[0]
        data['title'] = bmv['title']
        data['rang'] = 'Mémoire majeure'
        data['tierce'] = 'laeva_ejus'
        data['prayers_mg'] = 'bmv_{}'.format(bmv['cm'])
        data['proper_readings'] = False
        data['preface_id'] = Preface.objects.get(ref='marie_1').id

    return data
