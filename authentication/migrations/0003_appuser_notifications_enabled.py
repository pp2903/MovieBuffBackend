# Generated by Django 5.0.2 on 2024-02-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_appuser_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='notifications_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
