# Generated by Django 4.0.4 on 2022-05-16 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_dispositivos_cantidad_registros_dispositivos_puerto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cliente', models.CharField(max_length=50)),
                ('Proyecto', models.CharField(max_length=50)),
                ('IP', models.CharField(max_length=20)),
                ('Registros', models.IntegerField(default=0)),
                ('Cantidad_Registros', models.IntegerField(default=0)),
                ('Puerto', models.IntegerField(default=0)),
                ('ID_Labview', models.CharField(max_length=50)),
            ],
        ),
    ]