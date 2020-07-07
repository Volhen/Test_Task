from django import forms
from django.db import models
from django.forms import ClearableFileInput
from mainapp.models import Film, FileFilm


class FilmEditForm(forms.ModelForm):
    class Meta:
        model = Film
        # fields = '__all__'
        exclude = ('category', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FileModelForm(forms.ModelForm):
    class Meta:
        model = FileFilm
        fields = ['picture_gallery']
        widget = {
            'picture_gallery': ClearableFileInput(attrs={'multiple': True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['multiple'] = 'form-control'
