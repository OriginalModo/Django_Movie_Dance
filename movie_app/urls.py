
from django.urls import path
from .views import *

urlpatterns = [
    path('', show_all_movie),
    path('movie/<int:id_movie>', show_one_movie, name='one_movie'),
]
