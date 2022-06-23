from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_sensors_data', views.all_sensors_data, name='all_sensors_data'),
    path('all_sensors_temp', views.all_sensors_temp, name='all_sensors_temp'),
    path('sensor_1_data', views.sensor_1_data, name='sensor_1_data'),
    path('sensor_2_data', views.sensor_2_data, name='sensor_2_data'),
    path('update_sensor/<int:sensor_id>', views.update_sensor, name='update_sensor'),
    path('search_sensordata_by_macaddr', views.search_sensordata_by_macaddr, name='search_sensordata_by_macaddr'),
    path('search_sensordata_by_datetime', views.search_sensordata_by_datetime, name='search_sensordata_by_datetime'),
    path('export_sensordata_to_csv', views.export_sensordata_to_csv, name='export_sensordata_to_csv'),
]
