from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(blank=True)

class Measurement(models.Model):
    sensor_id = models.ManyToManyField(Sensor, related_name='measurements')
    temp = models.FloatField(default=0.00)
    datetime = models.DateTimeField(auto_now_add=True)