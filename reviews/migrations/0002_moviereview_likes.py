# Generated by Django 2.2.2 on 2019-07-08 20:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviereview',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='review_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
