# Generated by Django 3.2.8 on 2021-10-23 17:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference', '0001_initial'),
        ('app_production', '0006_auto_20211023_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='end_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 19, 30, 53, 79449)),
        ),
        migrations.AlterField(
            model_name='process',
            name='start_process',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 19, 30, 53, 79449)),
        ),
        migrations.AlterField(
            model_name='product',
            name='reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_reference.reference'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('-', '---'), ('OK', 'OK'), ('NOK', 'NOK')], default='-', max_length=3),
        ),
    ]
