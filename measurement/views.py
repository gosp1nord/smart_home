# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorsSerializer


class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        Sensor.objects.create(title=request.data['title'], description=request.data['description'])
        return Response({'status': 'OK'})


class SensorRetrieveView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


@api_view(['POST'])
def temperature_create_view(request):
    if request.method == 'POST':
        sensor = Sensor.objects.filter(id=request.data['id'])[0]
        Measurement.objects.create(di_sensor=sensor, temperature=request.data['temperature'])
        return Response({'status': 'OK'})


