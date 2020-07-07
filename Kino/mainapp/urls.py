from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.index, name='index'),
    path('poster/', mainapp.poster, name='poster'),
    path('film<int:pk>/', mainapp.film, name='film'),
]
