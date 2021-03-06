# Generated by Django 3.2.8 on 2021-10-24 09:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_production', '0021_auto_20211024_1142'),
        ('app_machine', '0021_alter_pallet_register_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detect_time', models.DateTimeField(default=datetime.datetime(2021, 10, 24, 11, 42, 39, 375405))),
                ('end_time', models.DateTimeField(default=datetime.datetime(2021, 10, 24, 11, 42, 39, 375405))),
                ('operator', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('0', '---'), ('1', 'SAFETY'), ('2', 'MEDIA'), ('3', 'PROCESS'), ('4', 'PART DEFECT')], default='0', max_length=1)),
                ('code', models.CharField(default='0', max_length=10)),
                ('pallet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_machine.pallet')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_production.product')),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_machine.station')),
            ],
        ),
    ]
