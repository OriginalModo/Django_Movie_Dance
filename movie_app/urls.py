
from django.urls import path
from .views import *

urlpatterns = [
    path('', show_all_movie),
    path('movie/<slug:slug_movie>', show_one_movie, name='one_movie'),
    # path('directors/', show_all_directors, name='all_directors'),
    # path('directors/', DirectorList.as_view(), name='all_directors'),
    path('directors/', ListView.as_view(model=Director, template_name='movie_app/all_directors.html'),
         name='all_directors'),
    # path('directors/<int:dir_id>', show_one_director, name='one_director'),
    # path('directors/<int:pk>', DirectorDetail.as_view(), name='one_director'),
    path('directors/<int:pk>', DetailView.as_view(
        template_name='movie_app/one_director.html', model=Director,
    ), name='one_director'),
    # path('actors/', show_all_actors, name='all_actors'),
    # path('actors/', ActorList.as_view(), name='all_actors'),
    path('actors/', ListView.as_view(model=Actor, template_name='movie_app/all_actors.html'),
         name='all_actors'),
    # path('actors/<slug:slug>', ActorDetail, name='one_actor'),
    # path('actors/<slug:actor_id>', show_one_actor, name='one_actor'),
    path('actors/<slug:pk>', DetailView.as_view(model=Actor, template_name='movie_app/one_actor.html'),
         name='one_actor'),
]
