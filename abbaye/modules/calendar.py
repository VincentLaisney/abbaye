""" Module calendar. """

import datetime
from math import floor

from apps.livrets.models import Day


def get_first_sunday_of_advent(year):
    """ Return the date of 1st Sunday of Advent for the given civil year. """
    christmas_date = datetime.date(year, 12, 25)
    christmas_weekday = christmas_date.weekday()
    return christmas_date - datetime.timedelta(days=(christmas_weekday + 22))


def get_liturgical_year(date):
    """ Return the liturgical year of the given date. """
    first_sunday_of_advent = get_first_sunday_of_advent(date.year)
    return (date.year if date < first_sunday_of_advent else (date.year + 1))


def get_easter(year):
    """ Returns the Easter date for the given liturgical year. """
    v1 = year - 1900
    v2 = v1 % 19
    v3 = (((v2 * 7) + 1) // 19)
    v4 = ((v2 * 11) + 4 - v3) % 29
    v5 = (v1 // 4)
    v6 = (v1 + v5 + 31 - v4) % 7
    v7 = 25 - v4 - v6
    easter_day = v7 if v7 > 0 else (31 + v7)
    easter_month = 4 if v7 > 0 else 3
    return datetime.date(year, easter_month, easter_day)


def get_tempo(date):
    """ Returns the tempo ref according to the given date. """

    weekday = (date.weekday() + 1) if date.weekday() != 6 else 0
    liturgical_year = get_liturgical_year(date)
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
    tempo = None
    if first_sunday_of_advent <= date < christmas:
        days = (date - first_sunday_of_advent).days
        week = floor((days / 7) + 1)
        tempo = 'adv_{}_{}'.format(week, weekday)
    elif christmas <= date < baptism_of_christ:
        # TODO: À affiner (ici, seulement les jours après Noël et la Ste Famille "dimanche" (cas le plus fréquent)).
        # Cas de la Ste Famille le 30 ('ste_famille_fer').
        # Féries après le 1er janvier jusqu'au Baptême ('noel_time_2' et 'noel_time_3').
        if weekday == 0:
            tempo = 'ste_famille_dim'
        else:
            tempo = 'noel_time_1'
    elif baptism_of_christ <= date < ash:
        days = (date - baptism_of_christ).days
        week = floor((days/7)+1)
        tempo = 'pa_{}_{}'.format(week, weekday)
    elif ash <= date < easter:
        days = (date - ash).days
        if days < 4:
            tempo = 'cendres_{}'.format(days)
        else:
            week = floor(((days + 3)/7))
            tempo = 'qua_{}_{}'.format(week, weekday)
    elif easter <= date <= pentecost:
        days = (date - easter).days
        week = floor((days/7)+1)
        tempo = 'tp_{}_{}'.format(week, weekday)
    elif pentecost <= date < first_sunday_of_next_advent:
        if date == pentecost + datetime.timedelta(days=7):
            tempo = 'trinite'
        elif date == pentecost + datetime.timedelta(days=11):
            tempo = 'fete_dieu'
        elif date == pentecost + datetime.timedelta(days=19):
            tempo = 'sacre_coeur'
        elif date == pentecost + datetime.timedelta(days=20):
            tempo = 'icm'
        elif date == christ_king:
            tempo = 'christ_roi'
        else:
            days = (first_sunday_of_next_advent - date).days
            week = 35 - floor(
                (days / 7) + (1 if weekday != 0 else 0)
            )
            tempo = 'pa_{}_{}'.format(week, weekday)
    return tempo


def get_sancto(date):
    """ Returns the sancto ref according to the given date. """
    month = date.strftime('%m')
    day = date.strftime('%d')
    sancto = '{}{}'.format(month, day)
    weekday = (date.weekday() + 1) if date.weekday() != 6 else 0
    if sancto in ['0202', '0806', '0914', '1109']:
        if weekday == 0:
            sancto += '_dim'
        else:
            sancto += '_fer'
    if sancto == '1209' and weekday == 1:
        sancto = '1208'
    return sancto


def get_liturgical_day(date):
    """ Returns the winner after comparison of forces. """
    tempo = get_tempo(date)
    tempo_force = Day.objects.filter(ref=tempo).first().precedence
    sancto = get_sancto(date)
    sancto_queryset = Day.objects.filter(ref=sancto)
    sancto_force = sancto_queryset.first().precedence if sancto_queryset else 0
    if sancto_force:
        if tempo_force > sancto_force:
            liturgical_day = tempo
        else:
            liturgical_day = sancto
    else:
        sancto = None
        liturgical_day = tempo
    return (tempo, sancto, liturgical_day)
