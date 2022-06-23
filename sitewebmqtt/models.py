from django.db import models

class Sensor(models.Model):
    macaddr = models.CharField(unique=True, max_length=12)
    piece = models.CharField(max_length=50)
    emplacement = models.CharField(max_length=50, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom


    class Meta:
        managed = False
        db_table = 'sensor'


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, models.DO_NOTHING)
    datetime = models.DateTimeField()
    temp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sensor_data'
