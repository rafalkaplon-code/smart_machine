# Generated by Django 3.2.8 on 2021-10-29 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_production', '0039_auto_20211025_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='end_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 14, 38, 2, 187637)),
        ),
        migrations.AlterField(
            model_name='process',
            name='start_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 14, 38, 2, 187637)),
        ),
    ]
