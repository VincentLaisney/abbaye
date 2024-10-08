""" apps/livrets/views.py """

import datetime
from math import ceil
import os
from pathlib import Path
import re
from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import render

from modules.calendar import get_liturgical_day

from .models import BMV, Day, Preface, Score


def home(request):
    """ Home page of Livrets. """
    return render(
        request,
        'livrets/home.html',
        {
            'number_of_days': range(1, 8),
        },
    )


def score(request):
    """ Check whether score exists and where. """
    request_get = request.GET
    TYPES = {
        'IN': 'introit',
        'GR': 'graduel',
        'AL': 'alleluia',
        'OF': 'offertoire',
        'CO': 'communion',
    }
    path = '{}livrets/data/GR/{}/{}.gabc'.format(
        settings.STATIC_ROOT,
        TYPES[request_get['type']],
        request_get['score'],
    )
    if Score.objects.filter(type=request_get['type'], ref=request_get['score']):
        if os.path.isfile(path):
            color = 'purple'
            title = "Cette partition se trouve dans le Missel grégorien ET comme fichier Gregorio."
        else:
            color = 'blue'
            title = "Cette partition se trouve dans le Missel grégorien."

    elif os.path.isfile(path):
        color = 'green'
        title = "Cette partition ne se trouve pas dans le Missel grégorien mais existe comme fichier Gregorio."
    else:
        color = 'red'
        title = "Cette partition ne se trouve ni dans le Missel grégorien ni comme fichier Gregorio."
    return JsonResponse(
        {
            'color': color,
            'title': title,
        }
    )


def pdf(request):
    """ Create the PDF of the booklet. """
    request_get = request.GET
    mode = request_get['mode']
    start = request_get['start'].split('/')
    start = datetime.date(int(start[2]), int(start[1]), int(start[0]))
    number_of_days = int(request_get['number_of_days'])

    tierce_psaumes = {
        '2': '0',
        '4': '1',
        '6': '2',
        '9': '3',
        '12': '4',
        '15': '5',
        '17': '6',
    }

    tex = ""
    tex = "\\input{config.tex}\n\n"
    tex += "\\begin{document}\n\n"
    tex += "\\setlength{\\columnseprule}{0.5pt}\n"
    tex += "\\colseprulecolor{rougeliturgique}\n\n"
    tex += "\\thispagestyle{empty}\n\n"
    tex += "\\begin{center}\n"
    tex += "+\\par\n"
    tex += "PAX\\par\n"
    tex += "\\vspace{.5cm}\n"
    tex += "\\TitreB{Abbaye Saint-Joseph de Clairval}\n"
    tex += "\\end{center}\n\n"
    tex += "\\TitreA{Messe conventuelle}\n"
    for i in range(number_of_days):
        date = start + datetime.timedelta(days=i)
        year_cycle = ['A', 'B', 'C'][(date.year - 2020) % 3]
        year_even = 2 if date.year % 2 == 0 else 1
        data_tempo, data_sancto, liturgical_day = get_data(date)
        data = data_tempo
        data['readings'] = data['ref']
        if data_sancto:
            if liturgical_day == data_sancto['ref']:
                data = data_sancto
                if data['proper_readings']:
                    data['readings'] = data_sancto['ref']
                else:
                    data['readings'] = data_tempo['ref']
                if not data['readings_cycle']:
                    data['readings_cycle'] = data_tempo['readings_cycle']
                if not data['preface_id']:
                    data['preface_id'] = data_tempo['preface_id']
        # BMV samedi:
        if date.weekday() == 5 and data['precedence'] < 30:
            ref_bmv = 'icm' if date.day < 8 \
                else '{}_{}'.format(
                    date.month,
                    ceil(date.day / 7),
                )
            bmv = BMV.objects.filter(ref=ref_bmv).values()[0]
            data['ref'] = 'bmv_{}'.format(bmv['cm'])
            data['title'] = bmv['title']
            data['rang'] = 'Mémoire majeure'
            data['tierce'] = 'laeva_ejus'
            data['prayers_mg'] = None
            data['preface_id'] = 'cm_{}'.format(bmv['cm'])

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
            if introit and mode == 'mg':
                tex += "\\TitreB{{Antienne d\'Introït~:}}\\Normal{{\\textit{{{}}} (p. {}).}}\\par\n".format(
                    introit.name,
                    introit.page,
                )
            else:
                tex += "\\TitreB{Antienne d\'Introït~:}\\par\\par\n"
                tex += "\\PartocheWithTraduction{{GR/introit/{}}}\\par\n".format(
                    grid_in,
                )

        # Ouverture:
        if mode == 'mg':
            tex += "\\TitreB{Ouverture de la célébration~:}\\Normal{p. 7.}\\par\n"
        else:
            tex += "\\TitreB{{Ouverture de la célébration~:}}\\input{{{}livrets/data/ordinaire/ouverture.tex}}\n".format(
                settings.STATIC_ROOT,
            )

        # Asperges me:
        if date.weekday() == 6:
            # TODO: if mode 'full'…
            if re.search('^tp_', data['ref']):
                tex += "\\TitreB{Vidi aquam}\\Normal{(p. 71).}\\par\n"
            elif re.search('^adv_', data['ref']) or re.search('^qua_', data['ref']):
                tex += "\\TitreB{Asperges me II}\\Normal{(p. 71).}\\par\n"
            elif date.day < 8 or data['rang'] in ['Fête', 'Solennité']:
                tex += "\\TitreB{Asperges me}\\Normal{(p. 70).}\\par\n"
            else:
                tex += "\\TitreB{Asperges me I}\\Normal{(p. 71).}\\par\n"

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
        if mode == 'mg':
            tex += "\\TierceMG{{{}}}{{{}}}\\par\n".format(
                tierce_antiphon,
                tierce_page,
            )
        else:
            tex += "\\TierceComplet{{{tierce_antiphon}}}{{{tierce_psaumes}}}\n".format(
                tierce_antiphon=tierce_antiphon,
                tierce_psaumes=tierce_psaumes[tierce_page],
            )

        # Kyrie:
        grid_ky = request_get['ky_' + str(i + 1)]
        if grid_ky:
            kyrie = Score.objects.filter(
                type='KY',
            ).filter(
                ref=grid_ky
            ).first()
            if kyrie:
                if mode == 'mg':
                    tex += "\\TitreB{{{}}}\\Normal{{(p. {}).}}\\par\n".format(
                        kyrie.name,
                        kyrie.page,
                    )
                else:
                    tex += "\\Partoche{{/GR/kyrie/{}}}\n".format(
                        grid_ky,
                    )
                    tex += "\\Traduction{{2cm}}{{\\input{{{}livrets/data/GR/ordinaire/kyrie.tex}}}}\n".format(
                        settings.STATIC_ROOT,
                    )

        # Gloria:
        grid_gl = request_get['gl_' + str(i + 1)]
        if grid_gl:
            gloria = Score.objects.filter(
                type='GL',
            ).filter(
                ref=grid_gl
            ).first()
            if gloria:
                if mode == 'mg':
                    tex += "\\TitreB{{{}}}\\Normal{{(p. {}).}}\\par\n".format(
                        gloria.name,
                        gloria.page,
                    )
                else:
                    tex += "\\Partoche{{/GR/gloria/{}}}\n".format(
                        grid_gl,
                    )
                    tex += "\\Traduction{{2cm}}{{\\input{{{}livrets/data/GR/ordinaire/gloria.tex}}}}\n".format(
                        settings.STATIC_ROOT,
                    )

        # Prayer Collecte:
        if data['prayers_mg'] and mode == 'mg':
            tex += "\\TitreB{{Oraison~:}}\\Normal{{p. {}.}}\\par\n".format(
                data['prayers_mg'].split('/')[0]
            )
        else:
            tex += "\\Oraison{{Oraison}}{{1}}{{{}}}\\par\n".format(
                data['ref'],
            )

        # First reading:
        tex += "\\Lecture{{Première lecture}}{{{}".format(
            data['readings'],
        )
        if data['readings_cycle'] == 6:
            tex += "_1_{}_{}}}\\par\n".format(
                year_cycle,
                year_even,
            )
        elif data['readings_cycle'] == 3:
            tex += "_{}_1}}\\par\n".format(
                year_cycle,
            )
        elif data['readings_cycle'] == 2:
            tex += "_1_{}}}\\par\n".format(
                year_even,
            )
        elif data['readings_cycle'] == 1:
            tex += "_1}\\par\n"

        # Graduel:
        grid_gr = request_get['gr_' + str(i + 1)]
        if grid_gr:
            graduel = Score.objects.filter(
                type='GR',
            ).filter(
                ref=grid_gr
            ).first()
            if graduel and mode == 'mg':
                tex += "\\TitreB{{Graduel~:}}\\Normal{{\\textit{{{}}} (p. {}).}}\\par\n".format(
                    graduel.name,
                    graduel.page,
                )
            else:
                tex += "\\TitreB{Graduel~:}\\par\n"
                tex += "\\PartocheWithTraduction{{GR/graduel/{}}}\\par\n".format(
                    grid_gr,
                )

        # Second reading (if both gr and al) and alleluia:
        grid_al = request_get['al_' + str(i + 1)]
        if grid_al:
            if grid_gr:
                # Second reading:
                tex += "\\Lecture{{Deuxième lecture}}{{{}".format(
                    data['readings'],
                )
                if data['readings_cycle'] == 6:
                    tex += "_2_{}_{}}}\\par\n".format(
                        year_cycle,
                        year_even,
                    )
                elif data['readings_cycle'] == 3:
                    tex += "_{}_2}}\\par\n".format(
                        year_cycle,
                    )
                elif data['readings_cycle'] == 2:
                    tex += "_2_{}}}\\par\n".format(
                        year_even,
                    )
                elif data['readings_cycle'] == 1:
                    tex += "_2}\\par\n"

            # Alleluia:
            alleluia = Score.objects.filter(
                type='AL',
            ).filter(
                ref=grid_al
            ).first()
            if alleluia and mode == 'mg':
                tex += "\\TitreB{{Alléluia~:}}\\Normal{{\\textit{{{}}} (p. {}).}}\\par\n".format(
                    alleluia.name,
                    alleluia.page,
                )
            else:
                tex += "\\TitreB{Alléluia~:}\\par\n"
                tex += "\\PartocheWithTraduction{{GR/alleluia/{}}}\n".format(
                    grid_al,
                )

        # Sequence:
        if data['sequence']:
            # TODO: if mode 'full'…
            tex += "\\TitreB{Séquence~:}\\par\n"
            tex += "\\PartocheWithTraduction{{GR/sequences/{}}}\n".format(
                data['sequence']
            )

        # Gospel:
        tex += "\\Lecture{{Évangile}}{{{}".format(
            data['readings'],
        )
        if data['readings'].startswith('pa_') and not data['readings'].endswith('_0'):
            tex += "_ev}\\par\n"
        elif data['readings_cycle'] == 6:
            tex += "_ev_{}_{}}}\\par\n".format(
                year_cycle,
                year_even,
            )
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

        # Credo:
        grid_cr = request_get['cr_' + str(i + 1)]
        if grid_cr:
            credo = Score.objects.filter(
                type='CR',
            ).filter(
                ref=grid_cr
            ).first()
            if credo:
                if mode == 'mg':
                    tex += "\\TitreB{{{}}}\\Normal{{(p. {}).}}\\par\n".format(
                        credo.name,
                        credo.page,
                    )
                else:
                    tex += "\\Partoche{{/GR/credo/{}}}\n".format(
                        grid_gl,
                    )
                    tex += "\\Traduction{{2cm}}{{\\input{{{}livrets/data/GR/ordinaire/credo.tex}}}}\n".format(
                        settings.STATIC_ROOT,
                    )

        # Offertoire:
        grid_of = request_get['of_' + str(i + 1)]
        if grid_of:
            offertoire = Score.objects.filter(
                type='OF',
            ).filter(
                ref=grid_of
            ).first()
            if offertoire and mode == 'mg':
                tex += "\\TitreB{{Antienne d\'offertoire~:}}\\Normal{{\\textit{{{}}} (p. {}).}}\\par\n".format(
                    offertoire.name,
                    offertoire.page,
                )
            else:
                tex += "\\TitreB{Antienne d\'offertoire~:}\\par\\par\n"
                tex += "\\PartocheWithTraduction{{GR/offertoire/{}}}\\par\n".format(
                    grid_of,
                )

        # Orate fratres :
        if (mode == "Livret complet"):
            tex += "\\TitreB{Offertoire~:}\n\n"
            tex += "\\Rubrique{Après l'encensement de l'autel (et des fidèles s'il y a lieu), le célébrant s'adresse aux fidèles en ces termes~:}\n"
            tex += "\\input{{{}livrets/data/ordinaire/offertoire.tex}}}}\n".format(
                settings.STATIC_ROOT,
            )

        # Prayer Super oblata:
        if data['prayers_mg']:
            tex += "\\TitreB{{Prière sur les offrandes~:}}\\Normal{{p. {}.}}\\par\n".format(
                data['prayers_mg'].split('/')[1],
            )
        else:
            tex += "\\Oraison{{Prière sur les offrandes}}{{2}}{{{}}}\\par\n".format(
                data['ref'],
            )

        # Preface:
        if str(data['preface_id']).startswith('cm_'):
            tex += "\\Preface{{Préface propre}}{{{}}}\\par\n".format(
                data['preface_id']
            )
        else:
            preface = Preface.objects.get(pk=data['preface_id'])
            if preface.page and mode == 'mg':
                tex += "\\TitreB{{{}~:}}\\Normal{{p. {}.}}\\par\n".format(
                    preface.name,
                    preface.page,
                )
            else:
                if data['preface_name_latin']:
                    tex += "\\PrefaceWithName{{{}}}{{{}}}{{{}}}{{{}}}\\par\n".format(
                        preface.name,
                        preface.ref,
                        data['preface_name_latin'],
                        data['preface_name_french'],
                    )
                else:
                    tex += "\\Preface{{{}}}{{{}}}\\par\n".format(
                        preface.name,
                        preface.ref,
                    )

        # Sanctus:
        grid_sa = request_get['sa_' + str(i + 1)]
        if grid_sa:
            sanctus = Score.objects.filter(
                type='SA',
            ).filter(
                ref=grid_sa
            ).first()
            if sanctus:
                if mode == 'mg':
                    tex += "\\TitreB{{{}}}\\Normal{{(p. {}).}}\\par\n".format(
                        sanctus.name,
                        sanctus.page,
                    )
                else:
                    tex += "\\Partoche{{/GR/sanctus/{}}}\n".format(
                        grid_gl,
                    )
                    tex += "\\Traduction{{2cm}}{{\\input{{{}livrets/data/GR/ordinaire/sanctus.tex}}}}\n".format(
                        settings.STATIC_ROOT,
                    )

        # Canon:
        if mode == 'mg':
            tex += "\\TitreB{Prière eucharistique n. 1}\\Normal{(p. 22).}\\par\n"
            tex += "\\TitreB{Rites de communion~:}\\Normal{p. 41.}\\par\n"
        else:
            tex += "\\Image{canon}{8cm}{3cm}\n"
            tex += "\\TitreA{{Prière eucharistique n. 1}}\n\\input{{{}livrets/data/ordinaire/canon.tex}}\n".format(
                settings.STATIC_ROOT,
            )
            tex += "\\TitreB{{Rites de communion~:}}\\input{{{}livrets/data/ordinaire/pater.tex}}\n".format(
                settings.STATIC_ROOT,
            )

        # Agnus:
        grid_sa = request_get['sa_' + str(i + 1)]
        if grid_sa:
            agnus = Score.objects.filter(
                type='AG',
            ).filter(
                ref=grid_sa
            ).first()
            if agnus:
                if mode == 'mg':
                    tex += "\\TitreB{{{}}}\\Normal{{(p. {}).}}\\par\n".format(
                        agnus.name,
                        agnus.page,
                    )
                else:
                    tex += "\\Partoche{{/GR/agnus/{}}}\n".format(
                        grid_gl,
                    )
                    tex += "\\Traduction{{2cm}}{{\\input{{{}livrets/data/GR/ordinaire/agnus.tex}}}}\n".format(
                        settings.STATIC_ROOT,
                    )

        # Communion:
        grid_co = request_get['co_' + str(i + 1)]
        if grid_co:
            communion = Score.objects.filter(
                type='CO',
            ).filter(
                ref=grid_co
            ).first()
            if communion and mode == 'mg':
                tex += "\\TitreB{{Antienne de Communion~:}}\\Normal{{\\textit{{{}}} (p. {}).}}\\par\n".format(
                    communion.name,
                    communion.page,
                )
            else:
                tex += "\\TitreB{Antienne de Communion~:}\\par\\par\n"
                tex += "\\PartocheWithTraduction{{GR/communion/{}}}\\par\n".format(
                    grid_co,
                )

        # Prayer Postcommunion:
        if data['prayers_mg']:
            tex += "\\TitreB{{Prière après la Communion~:}}\\Normal{{p. {}.}}\\par\n".format(
                data['prayers_mg'].split('/')[2],
            )
        else:
            tex += "\\Oraison{{Prière après la Communion}}{{3}}{{{}}}\\par\n".format(
                data['ref'],
            )

        # TODO: Super populum (Carême).

        # Conclusion:
        if mode == 'mg':
            tex += "\\TitreB{Conclusion~:}{\\Normal{p. 47.}}\\par\n"
        else:
            tex += "\\TitreB{{Conclusion~:}}\\input{{{}livrets/data/ordinaire/conclusion.tex}}\n".format(
                settings.STATIC_ROOT,
            )

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

    tex += "\n\\end{document}\n\n"

    with open(os.path.join(Path(__file__).resolve().parent, 'tex/livret.tex'), 'w') as tex_file:
        tex_file.write(tex)
        command = "cd {base_dir}/apps/livrets/tex; lualatex --shell-escape livret.tex; cp livret.pdf {media_dir}/livrets".format(
            base_dir=settings.BASE_DIR,
            media_dir=settings.MEDIA_ROOT,
        )
        os.system(command)
    return JsonResponse(
        {'back': 'OK'},
    )


def get_data(date):
    """ Return the data of the given date. """
    tempo, sancto, liturgical_day = get_liturgical_day(date)
    data_tempo = Day.objects.filter(ref=tempo).values()[0]
    data_sancto = Day.objects.filter(ref=sancto).values()[
        0] if sancto else {}
    return (data_tempo, data_sancto, liturgical_day)
