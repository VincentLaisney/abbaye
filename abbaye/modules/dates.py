""" Module dates """

import datetime


def date_to_french_string(date):
    """ Converts a date into french format. """
    weekdays = ['Lundi', 'Mardi', 'Mercredi',
                'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    months = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin',
              'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    weekday = weekdays[date.weekday()]
    day = date.day if date.day != 1 else '1er'
    month = months[date.month - 1]
    year = date.year
    return '{} {} {} {}'.format(weekday, day, month, year)


def get_first_sunday_of_advent(year):
    """ Return the date of 1st Sunday of Advent for the given civil year. """
    christmas_date = datetime.date(year, 12, 25)
    christmas_weekday = christmas_date.weekday()
    return christmas_date - datetime.timedelta(days=(christmas_weekday + 22))


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
