# Generated by Django 2.2.3 on 2019-09-18 23:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20190918_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmoviereview',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 19, 0, 23, 28, 490982)),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 19, 0, 23, 28, 490982)),
        ),
    ]