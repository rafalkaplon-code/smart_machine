# Generated by Django 3.2.8 on 2021-10-30 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_maintenance', '0024_auto_20211030_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fault',
            name='detect_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 11, 32, 25, 815698)),
        ),
        migrations.AlterField(
            model_name='fault',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 11, 32, 25, 815698)),
        ),
    ]
