# Generated by Django 5.0.1 on 2024-02-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0008_alter_movie_genre_alter_tvshow_genre"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tvshow",
            name="release_date",
        ),
    ]