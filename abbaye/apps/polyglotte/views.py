""" apps/polyglotte/views.py """

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .forms import VerseForm
from .models import Verse


def home(request):
    """ Home view of Polyglotte: redirect to Gn 1. """
    return render(
        request,
        'polyglotte/home.html',
        {}
    )


def verses_list(request, **kwargs):
    """ Returns a list of verses. """
    # Requested verses:
    verses = Verse.objects.filter(
        book=kwargs['book'], chapter=kwargs['chapter']).order_by('verse')

    # Books:
    books = ['Gn', 'Ex', 'Lev', 'Num', 'Dt',
             'Jos', 'Jdc', 'Ru', '1 Reg', '2 Reg', '3 Reg', '4 Reg', '1 Par', '2 Par',
             'Esd', 'Neh', 'Tb', 'Jdt', 'Est',
             'Jb', 'Ps', 'Pr', 'Qo', 'Ct', 'Sap', 'Si',
             'Is', 'Jer', 'Lam', 'Ba', 'Ez', 'Dn',
             'Os', 'Jon', 'Am', 'Ab', 'Jl', 'Mi', 'Na', 'So', 'Ha', 'Ag', 'Za', 'Mal',
             '1 Ma', '2 Ma',
             'Mt', 'Mc', 'Lc', 'Jo', 'Ac',
             'Rm', '1 Co', '2 Co', 'Ga', 'Ep', 'Ph', 'Col',
             '1 Th', '2 Th', '1 Tim', '2 Tim', 'Tit', 'Phm', 'He',
             'Jc', '1 Pe', '2 Pe', '1 Jo', '2 Jo', '3 Jo', 'Judæ', 'Ap']

    # Chapters:
    chapters = []
    chapters_of_this_book = Verse.objects.filter(
        book=kwargs['book']).values('chapter')
    for item in chapters_of_this_book:
        if not item['chapter'] in chapters:
            chapters.append(item['chapter'])

    return render(request, 'polyglotte/list.html', {
        'verses': verses,
        'books': books,
        'chapters': chapters,
        'current_book': kwargs['book'],
        'current_chapter': kwargs['chapter'],
    })


def verse_update(request, **kwargs):
    """ Form of verses. """
    verse = get_object_or_404(
        Verse, book=kwargs['book'], chapter=kwargs['chapter'], verse=kwargs['verse'])

    if request.method == 'POST':
        form_verse = VerseForm(request.POST, instance=verse)
        if form_verse.is_valid:
            form_verse.save()
            return redirect(
                reverse(
                    'polyglotte:list',
                    kwargs={
                        'book': kwargs['book'],
                        'chapter': kwargs['chapter']
                    }
                )
            )

    else:
        form_verse = VerseForm(instance=verse)

    return render(
        request,
        'polyglotte/form.html',
        {
            'form': form_verse,
            'object': verse,
        }
    )


def search(request):
    """ Returns a set of verses containing a pattern. """
    if request.method == 'GET':
        if request.GET:
            verses = Verse.objects.filter(
                txt_latin__icontains=request.GET['pattern']
            )
            count = len(verses)
            verses = verses[:100]

            return render(
                request,
                'polyglotte/search.html', {
                    'verses': verses,
                    'count': count,
                    'pattern': request.GET['pattern'],
                }
            )

    return render(
        request,
        'polyglotte/search.html',
        {}
    )
