# Generated by Django 3.2.8 on 2021-11-01 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_maintenance', '0028_auto_20211101_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fault',
            name='detect_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 11, 26, 34, 726152)),
        ),
        migrations.AlterField(
            model_name='fault',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 11, 26, 34, 726152)),
        ),
    ]
