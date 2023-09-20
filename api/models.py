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
    

from django.db import IntegrityError, transaction

# 智慧插頭資訊
class SmartPlugRec(models.Model):
    id = models.AutoField(primary_key=True)
    timestmp = models.DateTimeField(unique=True)  # Make the timestamp column unique
    response = models.JSONField()

    class Meta:
        db_table = 'plug_info'
        ordering = ['-timestmp']

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # Ensure uniqueness by handling possible IntegrityError
        with transaction.atomic():
            try:
                super().save(*args, **kwargs)
            except IntegrityError:
                # 假如有重複資料塞進 table
                pass