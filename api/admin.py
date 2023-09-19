from django.contrib import admin
from api.models import Sensor


# Register your models here.


class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'source_mac', 'sensor_type', 'sensor_value', 'rec_date')


admin.site.register(Sensor, SensorAdmin)