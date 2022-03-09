from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)


class Measurement(models.Model):
    di_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.IntegerField()
    date_meas = models.DateField(auto_now_add=True)
    time_meas = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True)


