# Generated by Django 5.0.1 on 2024-02-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0002_movie_tvshow_favorite_moviescript_watchlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="movie",
            name="genre",
        ),
        migrations.RemoveField(
            model_name="tvshow",
            name="genre",
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(to="baseapp.genre"),
        ),
        migrations.AddField(
            model_name="tvshow",
            name="genres",
            field=models.ManyToManyField(to="baseapp.genre"),
        ),
    ]
