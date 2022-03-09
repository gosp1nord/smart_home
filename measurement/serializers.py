from rest_framework import serializers
from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы
class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description']


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['di_sensor', 'temperature', 'date_meas', 'time_meas', 'image']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description', 'measurements']


