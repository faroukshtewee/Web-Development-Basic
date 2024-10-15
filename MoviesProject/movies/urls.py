from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movies_list, name='moviesList'),
    path('createMovie/', views.movies_create, name='createMovie'),
    path('<slug:slug>/createReview/', views.reviews_create, name='createReview'),
    path('<slug:slug>/reviews/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    # path('deleteMovie/', views.delete_movie, name='deleteMovie'),
    path('<slug:slug>/delete/', views.delete_movie, name='delete_movie'),

    path('<slug:slug>/', views.movie_detail, name='detail'),
]
