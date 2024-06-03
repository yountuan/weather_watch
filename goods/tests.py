# tests.py

from django.test import TestCase
from .models import Sensors, Data, Alerts
from datetime import date

class SensorsModelTest(TestCase):

    def setUp(self):
        self.sensor = Sensors.objects.create(
            model='AQ Sensor Model 1',
            type='AQ',
            installation_dat=date(2023, 6, 1),
            status='Active'
        )

    def test_create_sensor(self):
        sensor_count = Sensors.objects.count()
        self.assertEqual(sensor_count, 1)
        self.assertEqual(self.sensor.model, 'AQ Sensor Model 1')

    def test_read_sensor(self):
        sensor = Sensors.objects.get(id=self.sensor.id)
        self.assertEqual(sensor.model, 'AQ Sensor Model 1')

    def test_update_sensor(self):
        self.sensor.status = 'Inactive'
        self.sensor.save()
        updated_sensor = Sensors.objects.get(id=self.sensor.id)
        self.assertEqual(updated_sensor.status, 'Inactive')

    def test_delete_sensor(self):
        self.sensor.delete()
        sensor_count = Sensors.objects.count()
        self.assertEqual(sensor_count, 0)

class DataModelTest(TestCase):

    def setUp(self):
        self.sensor = Sensors.objects.create(
            model='TM Sensor Model 1',
            type='TM',
            installation_dat=date(2023, 6, 2),
            status='Active'
        )
        self.data = Data.objects.create(
            sensor=self.sensor,
            temperature=25.0,
            humidity=60.0,
            wind_speed=5.0
        )

    def test_create_data(self):
        data_count = Data.objects.count()
        self.assertEqual(data_count, 1)
        self.assertEqual(self.data.temperature, 25.0)

    def test_read_data(self):
        data = Data.objects.get(id=self.data.id)
        self.assertEqual(data.temperature, 25.0)

    def test_update_data(self):
        self.data.temperature = 26.0
        self.data.save()
        updated_data = Data.objects.get(id=self.data.id)
        self.assertEqual(updated_data.temperature, 26.0)

    def test_delete_data(self):
        self.data.delete()
        data_count = Data.objects.count()
        self.assertEqual(data_count, 0)

class AlertsModelTest(TestCase):

    def setUp(self):
        self.sensor = Sensors.objects.create(
            model='WS Sensor Model 1',
            type='WS',
            installation_dat=date(2023, 6, 4),
            status='Active'
        )
        self.alert = Alerts.objects.create(
            sensor=self.sensor,
            description='Wind speed exceeding safe limits.'
        )

    def test_create_alert(self):
        alert_count = Alerts.objects.count()
        self.assertEqual(alert_count, 1)
        self.assertEqual(self.alert.description, 'Wind speed exceeding safe limits.')

    def test_read_alert(self):
        alert = Alerts.objects.get(id=self.alert.id)
        self.assertEqual(alert.description, 'Wind speed exceeding safe limits.')

    def test_update_alert(self):
        self.alert.description = 'Wind speed back to normal.'
        self.alert.save()
        updated_alert = Alerts.objects.get(id=self.alert.id)
        self.assertEqual(updated_alert.description, 'Wind speed back to normal.')

    def test_delete_alert(self):
        self.alert.delete()
        alert_count = Alerts.objects.count()
        self.assertEqual(alert_count, 0)
