# Generated by Django 3.2.8 on 2021-10-23 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_production', '0018_auto_20211024_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdatafield',
            name='name',
            field=models.CharField(default='field', max_length=25),
        ),
        migrations.AlterField(
            model_name='process',
            name='end_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 0, 14, 42, 186330)),
        ),
        migrations.AlterField(
            model_name='process',
            name='start_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 0, 14, 42, 186330)),
        ),
    ]
