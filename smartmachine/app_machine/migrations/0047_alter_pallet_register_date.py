# Generated by Django 3.2.8 on 2021-11-01 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_machine', '0046_alter_pallet_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pallet',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 11, 21, 18, 312439)),
        ),
    ]
