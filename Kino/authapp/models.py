from django.db import models
from django.contrib.auth.models import AbstractUser


class KinoUser(AbstractUser):
    avatar = models.ImageField(
        verbose_name='Аватар пользователя',
        upload_to='users_avatars', blank=True
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Возраст',
        default="30"
    )
    article_date = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True
    )
