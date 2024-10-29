# Generated by Django 5.0.4 on 2024-10-29 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='tipo_usuario',
            field=models.CharField(choices=[('admin', 'Administrador'), ('cliente', 'Cliente'), ('domiciliario', 'Domiciliario'), ('negocio', 'Negocio')], default='cliente', max_length=15),
        ),
    ]
