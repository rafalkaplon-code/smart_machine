# Generated by Django 3.2.8 on 2021-10-24 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fault',
            name='detect_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 11, 45, 32, 512958)),
        ),
        migrations.AlterField(
            model_name='fault',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 11, 45, 32, 512958)),
        ),
    ]
