# Generated by Django 2.2.3 on 2019-07-14 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suggestions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='memberID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='up_votes',
            field=models.ManyToManyField(blank=True, related_name='up_vote', to=settings.AUTH_USER_MODEL),
        ),
    ]