# Generated by Django 3.2.8 on 2021-10-24 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_production', '0027_auto_20211024_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='end_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 19, 37, 16, 816480)),
        ),
        migrations.AlterField(
            model_name='process',
            name='start_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 19, 37, 16, 816480)),
        ),
    ]
