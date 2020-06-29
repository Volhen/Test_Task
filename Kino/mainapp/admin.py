from django.contrib import admin
from .models import Film, FileFilm


class FileInline(admin.TabularInline):
    model = FileFilm


class FileAdmin(admin.ModelAdmin):
    inlines = [
        FileInline,
    ]


admin.site.register(Film, FileAdmin)
