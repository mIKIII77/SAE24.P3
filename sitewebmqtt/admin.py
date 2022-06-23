from lib2to3.pygram import pattern_grammar
from django.contrib import admin
from .models import Sensor, SensorData


admin.site.register(Sensor)
admin.site.register(SensorData)


# Register your models here.
