# Generated by Django 3.2.8 on 2021-11-01 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_production', '0046_auto_20211101_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='end_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 11, 21, 18, 314847)),
        ),
        migrations.AlterField(
            model_name='process',
            name='start_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 11, 21, 18, 314847)),
        ),
        migrations.AlterField(
            model_name='product',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 11, 21, 18, 312439)),
        ),
        migrations.AlterField(
            model_name='product',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 11, 21, 18, 312439)),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('-', '-'), ('OK', 'true'), ('NOK', 'false')], default='-', max_length=3),
        ),
    ]
