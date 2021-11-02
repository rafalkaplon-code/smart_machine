# Generated by Django 3.2.8 on 2021-10-24 10:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_maintenance', '0003_auto_20211024_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaultCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='0', max_length=10)),
                ('type', models.CharField(choices=[('0', '---'), ('1', 'SAFETY'), ('2', 'MEDIA'), ('3', 'PROCESS'), ('4', 'PART DEFECT')], default='0', max_length=1)),
                ('description', models.CharField(max_length=255)),
                ('solution', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='fault',
            name='type',
        ),
        migrations.AlterField(
            model_name='fault',
            name='detect_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 12, 41, 35, 344784)),
        ),
        migrations.AlterField(
            model_name='fault',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 12, 41, 35, 344784)),
        ),
        migrations.AlterField(
            model_name='fault',
            name='code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_maintenance.faultcode'),
        ),
    ]
