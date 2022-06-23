import csv
from datetime import datetime
from re import S
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.http import Http404,FileResponse
from . import models
import mimetypes
from django.contrib import admin
from sitewebmqtt.forms import SensorForm



def home(request):
    return render(request, 'home.html')


def all_sensors_data(request):
    sensors = models.Sensor.objects.all()
    sensor_data = models.SensorData.objects.all()
    return render(request, 'all_sensors_data.html', {'sensors': sensors, 'sensor_data': sensor_data})


def all_sensors_temp(request):
    sensors = models.Sensor.objects.all()
    sensor_data = models.SensorData.objects.all()
    return render(request, 'all_sensors_temp.html', {'sensors': sensors, 'sensor_data': sensor_data})


def sensor_1_data(request):
    sensor_data = models.SensorData.objects.filter(sensor_id=1)
    return render(request, 'sensor_1_data.html', {'sensor_data': sensor_data})

def sensor_2_data(request):
    sensor_data = models.SensorData.objects.filter(sensor_id=2)
    return render(request, 'sensor_2_data.html', {'sensor_data': sensor_data})

def update_sensor(request, sensor_id):
    sensor = get_object_or_404(models.Sensor, pk=sensor_id)
    if request.method == 'POST':
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all_sensors_data')
    else:
        form = SensorForm(instance=sensor)
    return render(request, 'update_sensor.html', {'form': form})

def search_sensordata_by_macaddr(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        sensor_data = models.SensorData.objects.filter(sensor__macaddr=searched)
        return render(request, 'search_sensordata_by_macaddr.html', { 'searched': searched, 'sensor_data': sensor_data})
    else:
        return render(request, 'search_sensordata_by_macaddr.html', {})

def search_sensordata_by_datetime(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        sensor_data = models.SensorData.objects.filter(datetime__contains=searched)
        return render(request, 'search_sensordata_by_datetime.html', { 'searched': searched, 'sensor_data': sensor_data})
    else:
        return render(request, 'search_sensordata_by_datetime.html', {})

def export_sensordata_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sensordata.csv"'
    writer = csv.writer(response)
    writer.writerow(['Le capteur','MAC du capteur','datetime', 'temp'])
    for sensordata in models.SensorData.objects.all():
        writer.writerow([sensordata.sensor, sensordata.sensor.macaddr, sensordata.datetime, sensordata.temp])
    return response

