# Generated by Django 5.0.7 on 2024-07-28 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_equipo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('objetivo', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'equipos',
            },
        ),
        migrations.CreateModel(
            name='Futbolista',
            fields=[
                ('id_futbolista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('estado', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'futbolista',
            },
        ),
        migrations.CreateModel(
            name='Historico_Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('id_equipo', models.ForeignKey(db_column='id_equipo', on_delete=django.db.models.deletion.CASCADE, to='Jugadores.equipos')),
                ('id_futbolista', models.ForeignKey(db_column='id_futbolista', on_delete=django.db.models.deletion.CASCADE, to='Jugadores.futbolista')),
            ],
            options={
                'db_table': 'historico_equipo',
            },
        ),
    ]
