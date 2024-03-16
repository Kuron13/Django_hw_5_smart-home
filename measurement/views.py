# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    def post(self, request):
        cont = request.data
        sensor = Sensor.objects.create(name=cont['name'], description=cont['description'])
        sensor.save()
        return Response({'status': 'Датчик добавлен'})

    def get(self, request):
        sensors = Sensor.objects.all()
        sensor = SensorSerializer(sensors, many=True)
        return Response(sensor.data)
class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        cont = request.data
        print(cont)
        if 'name' in cont.keys():
            sensor.name = cont['name']
        if 'description' in cont.keys():
            sensor.description = cont['description']
        sensor.save()
        return Response({'status': 'Изменение датчика прошло успешно'})

class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        cont = request.data
        measur = Measurement.objects.create(temp=cont['temperature'])
        measur.save()
        measur.sensor_id.add(cont['sensor'])
        return Response({'status': 'Измерение добавлено'})