# Generated by Django 5.0.4 on 2024-10-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportesIncidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_incidencia', models.CharField(choices=[('tecnica', 'Técnica'), ('operativa', 'Operativa'), ('logistica', 'Logística')], default='logistica', max_length=20)),
                ('descripcion', models.TextField()),
                ('fecha_reporte', models.DateTimeField()),
            ],
        ),
    ]
