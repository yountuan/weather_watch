from django.shortcuts import render
from rest_framework import viewsets
from .models import Sensors, Data, Alerts
from .serializers import SensorsSerializer, DataSerializer, AlertsSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes

class SensorsViewSet(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer
    permission_classes = [IsAuthenticated]

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]

class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer
    permission_classes = [IsAuthenticated]