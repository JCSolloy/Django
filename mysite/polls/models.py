from django.db import models

# Create your models here.

class Dispositivo(models.Model):
    Cliente = models.CharField(max_length=50)
    Proyecto = models.CharField(max_length=50)
    IP = models.CharField(max_length=20)
    Registros = models.PositiveIntegerField(default=0)
    Cantidad_de_Registros = models.PositiveIntegerField(default=0)
    Puerto = models.PositiveIntegerField(default=0)
    ID_Labview = models.CharField(max_length=50)
    Dispositivo_de_Comunicación = models.CharField(max_length=50)
    Marca_Sensor = models.CharField(max_length=50)
    Modelo_Sensor = models.CharField(max_length=50)
    Medición = models.CharField(max_length=50)
    Modbus_ID = models.PositiveIntegerField(default=0)
