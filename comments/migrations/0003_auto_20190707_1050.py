# Generated by Django 2.2.2 on 2019-07-07 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190703_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 10, 50, 1, 413491)),
        ),
    ]