from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import F, Sum, Max, Min, Avg, Count, Value
from django.views.generic import ListView, DetailView


def show_all_movie(request):
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget') + 100,
        ffff=F('rating') * F('year'),
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movie.html', context={
        'movies': movies,
        'agg': agg,
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', context={
        'movie': movie
    })


def show_one_director(request, dir_id: int):
    director = get_object_or_404(Director, id=dir_id)
    return render(request, 'movie_app/one_director.html', context={
        'director': director
    })


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', context={
        'directors': directors
    })


def show_one_actor(request, actor_id: int):
    actor = get_object_or_404(Actor, id=actor_id)
    return render(request, 'movie_app/one_actor.html', context={
        'actor': actor
    })


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', context={
        'actors': actors
    })


class DirectorList(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'


class ActorList(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'


class DirectorDetail(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director
    context_object_name = 'director'


class ActorDetail(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor
    context_object_name = 'actor'































