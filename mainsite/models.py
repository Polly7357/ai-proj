from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:  #針對表格做註記以最新日期排序-負向排序
        ordering = ('-pub_date',)

    def __str__(self):  #查詢回應一條詢息, 取代原本繼承的函
        return self.title #等同於 Post.title

class Beverage(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'beverage'

    def __str__(self):  
        return self.name 

class TimeElecRates(models.Model):
    desc = models.TextField(null=False)
    effect_date = models.IntegerField()
    rates = models.FloatField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'time_elec_rates'
        unique_together = [['desc', 'effect_date']]
        
        
class C2Rates(models.Model):
    h_id = models.AutoField(primary_key=True, blank=True, null=False)
    #wday_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wday_rate', blank=True, null=False)
    #wend_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wend_rate', blank=True, null=False)
    wday_rate = models.ForeignKey(TimeElecRates,
        on_delete=models.CASCADE,
        related_name='c2rates_wday'  # Custom related_name for wday_rate
    )
    wend_rate = models.ForeignKey(
        TimeElecRates,
        on_delete=models.CASCADE,
        related_name='c2rates_wend'  # Custom related_name for wend_rate
    )
    class Meta:
        managed = False
        db_table = 'c2_rates'


class C3Rates(models.Model):
    h_id = models.AutoField(primary_key=True, blank=True, null=False)
    #wday_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wday_rate', blank=True, null=False)
    #wend_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wend_rate', blank=True, null=False)
    wday_rate = models.ForeignKey(
        TimeElecRates,
        on_delete=models.CASCADE,
        related_name='c3rates_wday'
    )
    wend_rate = models.ForeignKey(
        TimeElecRates,
        on_delete=models.CASCADE,
        related_name='c3rates_wend'
    )

    class Meta:
        managed = False
        db_table = 'c3_rates'


class CdeTransport(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'cde_transport'

    def __str__(self):  
        return self.name


class CfpClass(models.Model):
    class_id = models.TextField(primary_key=True, blank=True, null=False)
    class_name = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'cfp_class'

    def __str__(self):  
        return self.name


class CfpSosClass(models.Model):
    cfp_sos_class_id = models.TextField(primary_key=True, blank=True, null=False)
    cfp_sos_class_name = models.TextField(blank=True, null=False)
    cfp_sub_class = models.ForeignKey('CfpSubClass', models.DO_NOTHING, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'cfp_sos_class'


class CfpSubClass(models.Model):
    sub_class_id = models.TextField(primary_key=True, blank=True, null=False)
    sub_class_name = models.TextField(blank=True, null=False)
    class_id = models.ForeignKey(CfpClass, models.DO_NOTHING, db_column='class_id', blank=True, null=False)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'cfp_sub_class'

class EggProds(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'egg_prods'

    def __str__(self):  
        return self.name


class ElecDeviceConsumption(models.Model):
    name = models.TextField(unique=True)
    watt = models.IntegerField(blank=True, null=False)
    date = models.DateTimeField(default=timezone.now)  

    class Meta:
        managed = False
        db_table = 'elec_device_consumption'

    def __str__(self):  
        return self.name


class Energy(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'energy'

    def __str__(self):  
        return self.name


class LactoseProds(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'lactose_prods'

    def __str__(self):  
        return self.name


class SummerC2Rates(models.Model):
    h_id = models.AutoField(primary_key=True, blank=True, null=False)
    #wday_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wday_rate', blank=True, null=False)
    #wend_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wend_rate', blank=True, null=False)
    wday_rate = models.ForeignKey(
        TimeElecRates,
        on_delete=models.CASCADE,
        related_name='summerc2rates_wday'
    )
    wend_rate = models.ForeignKey(
        TimeElecRates,
        on_delete=models.CASCADE,
        related_name='summerc2rates_wend'
    )

    class Meta:
        managed = False
        db_table = 'summer_c2_rates'


class SummerC3Rates(models.Model):
    h_id = models.AutoField(primary_key=True, blank=True, null=False)
    #wday_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wday_rate', blank=True, null=False)
    #wend_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wend_rate', blank=True, null=False)
    wday_rate = models.ForeignKey(
        TimeElecRates,
        on_delete=models.CASCADE,
        related_name='summerc3rates_wday'
    )
    wend_rate = models.ForeignKey(
        TimeElecRates,
        on_delete=models.CASCADE,
        related_name='summerc3rates_wend'
    )

    class Meta:
        managed = False
        db_table = 'summer_c3_rates'


from django.db import models, IntegrityError, transaction

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
                # Handle the case where a duplicate timestamp is encountered
                # You can log, raise an exception, or handle it as needed
                pass


