# Generated by Django 3.2.8 on 2021-10-24 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_maintenance', '0008_auto_20211024_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fault',
            name='detect_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 20, 41, 6, 184737)),
        ),
        migrations.AlterField(
            model_name='fault',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 20, 41, 6, 184737)),
        ),
    ]
