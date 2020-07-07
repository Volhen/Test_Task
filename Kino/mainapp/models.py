from django.db import models


class FilmCategory(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=64,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='Активна',
        db_index=True,
        default=True
    )

    def __str__(self):
        return self.name


class Film(models.Model):
    category = models.ForeignKey(
        FilmCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Название фильма',
        max_length=50
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    main_picture = models.ImageField(
        verbose_name='Главная картинка',
        upload_to='main_picture',
        blank=True
    )
    link_to_trailer = models.CharField(
        verbose_name='Ссылка на трейлер',
        max_length=200,
        blank=True
    )
    type_film_2d = models.BooleanField(
        verbose_name='2D',
        default=False
    )
    type_film_3d = models.BooleanField(
        verbose_name='3D',
        default=False
    )
    type_film_imax = models.BooleanField(
        verbose_name='IMAX',
        default=False
    )
    seo_url = models.CharField(
        verbose_name='URL',
        max_length=200,
        blank=True
    )
    seo_title = models.CharField(
        verbose_name='Title',
        max_length=129,
        blank=True
    )
    seo_Keywords = models.CharField(
        verbose_name='Keywords',
        max_length=129,
        blank=True
    )
    seo_description = models.TextField(
        verbose_name='Description',
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='активен',
        db_index=True,
        default=True
    )

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    @staticmethod
    def get_items():
        return Film.objects.filter(category__is_active=True, is_active=True).order_by('category', 'name')


class FileFilm(models.Model):
    picture_gallery = models.ImageField(
        verbose_name='Галерея картинок',
        upload_to='picture_gallery',
        blank=True
    )
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='images')
