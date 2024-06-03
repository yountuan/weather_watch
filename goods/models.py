from django.db import models

class Sensors(models.Model):
    SENSOR_TYPES = (
        ('AQ', 'Air Quality'),
        ('TM', 'Temperature'),
        ('PR', 'Pressure'),
        ('WS', 'Wind Speed'),
        ('WD', 'Wind Direction'),
        ('NO', 'Noise'),
        ('LT', 'Light'),
        ('UV', 'UV Index'),
    )
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=SENSOR_TYPES)
    installation_dat = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.model
    

class Data(models.Model):
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()

    def __str__(self) -> str:
        return f'{self.sensor} - at {self.timestamp}'
    
    
class Alerts(models.Model):
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f'Alert for {self.sensor} - at {self.timestamp}'



