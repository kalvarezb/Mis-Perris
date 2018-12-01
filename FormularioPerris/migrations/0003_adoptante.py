# Generated by Django 2.1.2 on 2018-11-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormularioPerris', '0002_auto_20181109_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=60)),
                ('run', models.CharField(max_length=11)),
                ('nombreCompleto', models.CharField(max_length=90)),
                ('pefechaNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=12)),
                ('region', models.CharField(max_length=30)),
                ('comuna', models.CharField(max_length=30)),
                ('tipoVivienda', models.CharField(choices=[('G', 'Casa con patio grande'), ('P', 'Casa con patio pequeño'), ('S', 'Casa sin patio'), ('D', 'Departamento')], default='G', max_length=1)),
            ],
        ),
    ]
