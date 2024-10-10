from django.contrib import admin

# Register your models here.
# Movies class in models.py
from .models import Movies, Reviews

# Register your models here.
# username: IMDB
# password: IMDB
admin.site.register(Movies)
admin.site.register(Reviews)