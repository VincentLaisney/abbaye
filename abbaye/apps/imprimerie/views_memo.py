""" apps/imprimerie/views_memo.py """

import os
import markdown as md

from django.shortcuts import render

from apps.main.decorators import group_required


@group_required('Imprimerie')
def memo(request):
    """ Memo imprimerie. """
    with open(
        os.path.dirname(os.path.abspath(__file__))
        + '/templates/imprimerie/memo/memo.md'
    ) as f:
        markdown = f.read()
    html = md.markdown(
        markdown,
        extensions=['markdown.extensions.fenced_code']
    )
    return render(
        request,
        'imprimerie/memo/memo.html',
        {
            'html': html,
        },
    )
