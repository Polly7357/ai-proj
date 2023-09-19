from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.


class Sensor(models.Model):
    source_mac = models.CharField(max_length=50)
    sensor_type = models.CharField(max_length=50)
    sensor_value = models.FloatField()
    rec_date = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ('-rec_date',)
   
    def __str__(self):
        return f"{self.rec_date}_{self.source_mac}"