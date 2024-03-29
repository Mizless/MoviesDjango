from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie



class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url" # по какому полю искать запись