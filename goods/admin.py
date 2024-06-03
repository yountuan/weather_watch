from django.contrib import admin
from .models import Data, Sensors, Alerts

admin.site.register(Data)
admin.site.register(Sensors)
admin.site.register(Alerts)
