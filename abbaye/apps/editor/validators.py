""" Validators for Editor. """

from django.core.exceptions import ValidationError


def ean13_validator(ean):
    """ Validate an EAN13 code. """
    # Check digits only:
    if not ean.isdecimal():
        raise ValidationError(
            'Veuillez entrer un code composé uniquement de chiffres.')

    # Check length:
    if len(ean) != 13:
        raise ValidationError(
            'Veuillez entrer un code EAN composé de 13 caractères exactement.')

    # Check the validation key:
    odd_sum = sum(int(digit) for digit in ean[0:11:2])
    even_sum = sum(int(digit) for digit in ean[1:12:2]) * 3
    key = (10 - ((odd_sum + even_sum) % 10)) % 10
    if int(ean[12]) != key:
        raise ValidationError(
            'Code faux \
            (somme des digits impairs = {}, \
            somme des digits pairs = {}, \
            le dernier digit devrait être {}).'
            .format(odd_sum, even_sum, key)
        )
