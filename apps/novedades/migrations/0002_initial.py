# Generated by Django 5.0.4 on 2024-10-28 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('novedades', '0001_initial'),
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='novedades',
            name='solicitud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solicitud.solicitud'),
        ),
    ]
