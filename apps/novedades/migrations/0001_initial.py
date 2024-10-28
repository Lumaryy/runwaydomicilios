# Generated by Django 5.0.4 on 2024-10-28 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('domiciliarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')], default='abierto', max_length=15)),
                ('fecha_reporte', models.DateTimeField()),
                ('domiciliario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='domiciliarios.domiciliarios')),
            ],
        ),
    ]
