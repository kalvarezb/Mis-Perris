# Generated by Django 2.1.2 on 2018-12-01 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormularioPerris', '0006_auto_20181201_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adoptante',
            old_name='comuna',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='adoptante',
            old_name='nombreCompleto',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='adoptante',
            old_name='run',
            new_name='rut',
        ),
    ]