from django import forms
from . import models


class CreateMovie(forms.ModelForm):
    class Meta:
        model = models.Movies
        fields = ['poster', 'title', 'slug', 'description', 'Director', 'Four_main_actors']


class CreateReview(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = ['review', 'feedback_stars']
        widgets = {
            'feedback_stars': forms.HiddenInput(),  # Use hidden input for the stars field
        }
