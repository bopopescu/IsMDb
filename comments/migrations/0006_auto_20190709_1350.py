# Generated by Django 2.2.2 on 2019-07-09 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_auto_20190709_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 13, 50, 32, 287694)),
        ),
    ]
