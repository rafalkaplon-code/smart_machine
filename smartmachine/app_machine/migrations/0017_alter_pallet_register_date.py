# Generated by Django 3.2.8 on 2021-10-23 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_machine', '0016_alter_pallet_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pallet',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 0, 8, 25, 2849)),
        ),
    ]
