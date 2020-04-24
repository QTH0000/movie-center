from django.views.generic import DetailView, ListView

from .models import Movie


class MovieDetailView(DetailView):
    model = Movie
    slug_url_kwarg = "the_slug"
    context_object_name = "movie"
    slug_field = "slug"
    template_name = "movie/movie_detail.html"


class MovieListView(ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "movie/movie_list.html"
    paginate_by = 10
