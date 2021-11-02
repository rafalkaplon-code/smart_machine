# Generated by Django 3.2.8 on 2021-10-23 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_production', '0004_auto_20211023_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='isNOK',
        ),
        migrations.RemoveField(
            model_name='product',
            name='isOK',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('-', 'Null'), ('OK', 'Part OK'), ('NOK', 'Part NOK')], default='-', max_length=3),
        ),
        migrations.AlterField(
            model_name='process',
            name='end_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 19, 14, 39, 372648)),
        ),
        migrations.AlterField(
            model_name='process',
            name='start_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 19, 14, 39, 372648)),
        ),
    ]
