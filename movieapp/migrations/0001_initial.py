# Generated by Django 5.0.2 on 2024-02-19 16:45

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='live_chanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=100)),
                ('video_url', models.URLField()),
                ('image', models.ImageField(upload_to='movie/image/')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('see', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('video_url', models.URLField()),
                ('image', models.ImageField(upload_to='movie/image/')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('see', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='channelviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livechannel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.live_chanel')),
            ],
        ),
        migrations.CreateModel(
            name='site_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ViewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('movie2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
