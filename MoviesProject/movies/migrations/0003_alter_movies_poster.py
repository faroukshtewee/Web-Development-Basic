# Generated by Django 4.2.16 on 2024-09-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movies_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster',
            field=models.ImageField(default='index.jpg', upload_to=''),
        ),
    ]
