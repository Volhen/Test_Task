from django.contrib import admin
from .models import Film, FileFilm, FilmCategory


class FileInline(admin.TabularInline):
    model = FileFilm


class FileAdmin(admin.ModelAdmin):
    inlines = [
        FileInline,
    ]


admin.site.register(Film, FileAdmin)
admin.site.register(FilmCategory)
