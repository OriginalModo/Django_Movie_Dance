
from django.urls import path
from .views import *

urlpatterns = [
    path('', show_all_movie),
    path('movie/<slug:slug_movie>', show_one_movie, name='one_movie'),
    # path('directors/', show_all_directors, name='all_directors'),
    path('directors/', DirectorView.as_view(), name='all_directors'),
    path('directors/<int:dir_id>', show_one_director, name='one_director'),
    # path('actors/', show_all_actors, name='all_actors'),
    path('actors/', ActorView.as_view(), name='all_actors'),
    path('actors/<slug:actor_id>', show_one_actor, name='one_actor'),
]
