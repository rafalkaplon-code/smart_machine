# Generated by Django 3.2.8 on 2021-10-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
