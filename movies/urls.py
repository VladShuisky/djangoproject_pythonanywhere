from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', view=views.MoviesView.as_view(), name='movies'),
    path('<slug:slug>/', view=views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie_api/', view=views.GetMoviesApiView.as_view(), name='movie_api'),
    path('review/<int:pk>/', view=views.AddReview.as_view(), name='add_review'),
    path('ckeditor/', include('ckeditor_uploader.urls')),  #редактор CKEditor

]
