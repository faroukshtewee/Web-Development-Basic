from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import Movies, Reviews
from . import forms


def movies_list(request):
    movies = Movies.objects.all().order_by('year_release')
    return render(request, "movies/movies_list.html", {'movies': movies})


def movie_detail(request, slug):
    # movie = Movies.objects.get(slug=slug)
    movie = get_object_or_404(Movies, slug=slug)
    reviews = movie.reviews.all()
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'movies': reviews})


@login_required(login_url="/accounts/login/")
def movies_create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = forms.CreateMovie(request.POST, request.FILES)
            if form.is_valid():
                # save to the data base
                instance = form.save(commit=False)
                instance.title = form.data.get("title")
                instance.save()
                return redirect('movies:moviesList')
        else:
            form = forms.CreateMovie()
        return render(request, 'movies/create_movie.html', {'form': form})
    else:
        return redirect('movies:moviesList')


@login_required(login_url="/accounts/login/")
def reviews_create(request, slug):
    movie = get_object_or_404(Movies, slug=slug)  # Get the movie using the slug
    if request.method == "POST":
        form = forms.CreateReview(request.POST, request.FILES)
        if form.is_valid():
            # save to the database
            instance = form.save(commit=False)
            instance.movie = movie
            instance.user = request.user
            instance.save()
            return redirect('movies:detail', slug=movie.slug)
    else:
        form = forms.CreateReview()
    return render(request, 'reviews/create_review.html', {'form': form, 'movie': movie})


def reviews_list(request):
    reviews = Reviews.objects.all()
    return render(request, "movies/movie_detail.html", {'movies': reviews})


@login_required(login_url="/accounts/login/")
def delete_review(request, slug, review_id):
    # Get the movie by slug (for redirection purposes)
    movie = get_object_or_404(Movies, slug=slug)

    # Get the review by ID
    review = get_object_or_404(Reviews, id=review_id)

    # Check if the user is the author of the review or an admin
    if request.user == review.user or request.user.is_staff:
        review.delete()
        return redirect('movies:detail', slug=movie.slug)  # Redirect after deletion
    else:
        # Optionally, you could raise a permission denied error or show a message
        return redirect('movies:detail', slug=movie.slug)


@login_required(login_url="/accounts/login/")
def delete_movie(request, slug):
    movie = get_object_or_404(Movies, slug=slug)

    if request.method == "POST":
        movie.delete()
        return redirect('movies:moviesList')

    return redirect('movies:moviesList')