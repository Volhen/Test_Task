import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),

    path('categories/', adminapp.categories, name='categories'),
    path('categories/detail/<int:pk>', adminapp.categories_detail, name='categories_detail'),
]
