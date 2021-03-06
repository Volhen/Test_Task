# Generated by Django 3.0.7 on 2020-06-30 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активна')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название фильма')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('main_picture', models.ImageField(blank=True, upload_to='main_picture', verbose_name='Главная картинка')),
                ('link_to_trailer', models.CharField(blank=True, max_length=200, verbose_name='Ссылка на трейлер')),
                ('type_film_2d', models.BooleanField(default=False, verbose_name='2D')),
                ('type_film_3d', models.BooleanField(default=False, verbose_name='3D')),
                ('type_film_imax', models.BooleanField(default=False, verbose_name='IMAX')),
                ('seo_url', models.CharField(blank=True, max_length=200, verbose_name='URL')),
                ('seo_title', models.CharField(blank=True, max_length=129, verbose_name='Title')),
                ('seo_Keywords', models.CharField(blank=True, max_length=129, verbose_name='Keywords')),
                ('seo_description', models.TextField(blank=True, verbose_name='Description')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='активен')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.FilmCategory')),
            ],
        ),
        migrations.CreateModel(
            name='FileFilm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_gallery', models.ImageField(blank=True, upload_to='picture_gallery', verbose_name='Галерея картинок')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Film')),
            ],
        ),
    ]
