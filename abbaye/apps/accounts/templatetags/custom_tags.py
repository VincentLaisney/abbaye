""" apps/accounts/templatetags/custom_tags.py """

from django import template

register = template.Library()


@register.filter
def url_after_next(url_to_split):
    """ Returns an url removing everything until 'next='. """
    return url_to_split.split('next=')[1]
