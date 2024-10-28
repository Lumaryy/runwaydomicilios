# Generated by Django 5.0.4 on 2024-10-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domiciliarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licencia_vehiculo', models.CharField(max_length=50)),
                ('disponibilidad', models.CharField(choices=[('disponible', 'Disponible'), ('ocupado', 'Ocupado'), ('no_disponible', 'No Disponible')], default='disponible', max_length=15)),
            ],
        ),
    ]
