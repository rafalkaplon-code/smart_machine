# Generated by Django 3.2.8 on 2021-10-23 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_machine', '0003_auto_20211023_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pallet',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 19, 5, 15, 790868)),
        ),
    ]
