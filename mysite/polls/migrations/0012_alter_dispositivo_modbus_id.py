# Generated by Django 4.0.4 on 2022-05-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_dispositivo_modbus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='Modbus_ID',
            field=models.PositiveIntegerField(default=0),
        ),
    ]