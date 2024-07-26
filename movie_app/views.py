from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import F, Sum, Max, Min, Avg, Count, Value


def show_all_movie(request):
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget')+100,
        ffff=F('rating')*F('year'),
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
