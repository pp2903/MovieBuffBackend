# Generated by Django 5.0.1 on 2024-02-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0009_remove_tvshow_release_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="tvshow",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
