# Generated by Django 5.0.2 on 2024-02-18 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_movie_video_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='movie',
        ),
    ]
