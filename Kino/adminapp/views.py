from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from authapp.models import KinoUser
from mainapp.models import FilmCategory, Film, FileFilm
from adminapp.forms import FilmEditForm, FileModelForm


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users_list = KinoUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')
    context = {
        'title': 'Панель администратора',
        'object_list': users_list
    }

    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda x: x.is_superuser)
def categories(request):

    object_list = FilmCategory.objects.filter(is_active=True)
    film = Film.objects.filter(is_active=True, category__is_active=True).order_by('name')

    context = {
        'title': 'Фильмы',
        'films': film,
        'categorys': object_list,
    }
    return render(request, 'adminapp/category_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def categories_detail(request, pk):

    film_object = get_object_or_404(Film, pk=pk)
    gallery = FileFilm.objects.filter(film=pk).all()
    picture_gallery = get_object_or_404(FileFilm, pk=pk)

    if request.method == 'POST':
        form_file = FileModelForm(request.POST, request.FILES, instance=picture_gallery)
        form = FilmEditForm(request.POST, request.FILES, instance=film_object)
        files = request.FILES.getlist('picture_gallery')
        if form.is_valid() and form_file.is_valid():
            form.save()
            for f in files:
                file_instance = FileFilm(picture_gallery=f, film=film_object)
                file_instance.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        form = FilmEditForm(instance=film_object)
        form_file = FileModelForm(instance=picture_gallery)

    context = {
        'title': 'Карточка фильма',
        'form': form,
        'form_file': form_file,
        'film_object': film_object,
        'gallery': gallery,
    }
    return render(request, 'adminapp/detail.html', context)
