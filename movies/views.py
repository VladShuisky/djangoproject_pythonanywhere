from django.shortcuts import render, redirect
from django.views.generic.base import View
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import ReviewForm


from .models import Movie


class MoviesView(View):

    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        return render(request, 'movies/movies.html', {'movie_list': movies})


class MovieDetailView(View):

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})


class GetMoviesApiView(APIView):

    def get(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(instance=queryset, many=True)
        return Response(serializer.data)


class AddReview(View):

    def post(self, request, pk):
        movie = Movie.objects.get(id=pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):  # если в пост запросе передалался id родительского отзыва(если он был помещен туда с помощью js при нажатии на кнопку ответить
                form.parent_id = int(request.POST.get('parent'))  # добавляется поле parent id к форме и дальше передается
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
