from django.shortcuts import render, get_object_or_404
from mainapp.models import Film, FileFilm
from django.urls import reverse


def index(request):

    context = {
        "page_title": 'Главная',
    }

    return render(request, 'mainapp/index.html', context)


def poster(request):

    film = Film.objects.all().order_by('name')

    context = {
        'page_title': 'Афиша',
        'films': film, 
    }
    return render(request, 'mainapp/poster.html', context)


def film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    picture_gallery = FileFilm.objects.filter(film=film).all()

    context = {
        'page_title': 'Страница фильма',
        'gallery': picture_gallery,
        'object': film,
    }
    return render(request, 'mainapp/film.html', context)
