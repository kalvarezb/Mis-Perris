# Generated by Django 2.1.2 on 2018-12-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormularioPerris', '0007_auto_20181201_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adoptante',
            old_name='pefechaNacimiento',
            new_name='fechaNacimiento',
        ),
        migrations.AddField(
            model_name='adoptante',
            name='apellidos',
            field=models.CharField(default='apellido', max_length=90),
        ),
    ]
