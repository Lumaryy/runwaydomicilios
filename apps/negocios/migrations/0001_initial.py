# Generated by Django 5.0.4 on 2024-10-28 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Negocios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('banner', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
    ]
