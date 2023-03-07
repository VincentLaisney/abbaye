""" modules/dates.py """


MONTHS = [
    (1, 'janvier'),
    (2, 'février'),
    (3, 'mars'),
    (4, 'avril'),
    (5, 'mai'),
    (6, 'juin'),
    (7, 'juillet'),
    (8, 'août'),
    (9, 'septembre'),
    (10, 'octobre'),
    (11, 'novembre'),
    (12, 'décembre'),
]


def date_to_french_string(date):
    """ Converts a date into french format. """
    weekdays = ['Lundi', 'Mardi', 'Mercredi',
                'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    months = [item[1] for item in MONTHS]
    weekday = weekdays[date.weekday()]
    day = date.day
    month = months[date.month - 1]
    year = date.year
    return '{} {} {} {}'.format(weekday, day, month, year)
