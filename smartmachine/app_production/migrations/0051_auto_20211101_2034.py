# Generated by Django 3.2.8 on 2021-11-01 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_production', '0050_auto_20211101_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='end_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 20, 34, 16, 824779)),
        ),
        migrations.AlterField(
            model_name='process',
            name='start_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 20, 34, 16, 824779)),
        ),
        migrations.AlterField(
            model_name='product',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 20, 34, 16, 824779)),
        ),
        migrations.AlterField(
            model_name='product',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 20, 34, 16, 824779)),
        ),
    ]
