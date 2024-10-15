from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movies(models.Model):
    poster = models.ImageField(default='index.jpg', blank=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.CharField(max_length=1500)
    Director = models.CharField(max_length=150)
    Four_main_actors = models.CharField(max_length=250)
    year_release = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    movie = models.ForeignKey(Movies, default=None, on_delete=models.CASCADE, related_name='reviews')
    year_release_review = models.DateTimeField(auto_now_add=True)
    feedback_stars = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.user} {self.review} {self.movie} {self.feedback_stars}'
