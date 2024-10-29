# Generated by Django 5.0.4 on 2024-10-29 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0003_alter_solicitud_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'PENDIENTE'), ('ASIGNADO', 'ASIGNADO'), ('EN CURSO', 'EN CURSO'), ('COMPLETADO', 'COMPLETADO'), ('REPROGRAMADO', 'REPROGRAMADO'), ('CANCELADO', 'CANCELADO')], default='PENDIENTE', max_length=12),
        ),
    ]
