# Generated by Django 4.2.16 on 2024-09-27 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movies'),
        ),
    ]
