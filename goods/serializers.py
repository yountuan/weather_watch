from rest_framework import serializers
from .models import Data, Alerts, Sensors

class SensorsSerializer(serializers.Serializer):
    class Meta:
        model = Sensors
        fields = '__all__'

class DataSerializer(serializers.Serializer):
    class Meta:
        model = Data
        fields = '__all__'

class AlertsSerializer(serializers.Serializer):
    class Meta:
        model = Alerts
        fields = '__all__'