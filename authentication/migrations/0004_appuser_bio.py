# Generated by Django 5.0.2 on 2024-02-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_appuser_notifications_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
