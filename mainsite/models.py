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

# 飲品
class Beverage(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        #managed = False
        db_table = 'beverage'

    def __str__(self):  
        return self.name 

# 電價表
class TimeElecRates(models.Model):
    desc = models.TextField(unique=True, null=False)
    effect_date = models.IntegerField()
    rates = models.FloatField(blank=True, null=False)

    class Meta:
        #managed = False
        db_table = 'time_elec_rates'
        unique_together = [['desc', 'effect_date']]
        
# 二段式費率表        
class C2Rates(models.Model):
    h_id = models.AutoField(primary_key=True, blank=True, null=False)
    #wday_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wday_rate', blank=True, null=False)
    #wend_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wend_rate', blank=True, null=False)
    wday_rate = models.ForeignKey('timeelecrates',  # Use the related model name as a string
    on_delete=models.CASCADE, db_column='wday_rate', related_name='C2Rates_wday', to_field='desc',   # Specify the column you want to reference
    )
    wend_rate = models.ForeignKey('timeelecrates',  # Use the related model name as a string
    on_delete=models.CASCADE, db_column='wend_rate', related_name='C2Rates_wend', to_field='desc',  # Specify the column you want to reference
    )
    # wday_rate = models.ForeignKey(TimeElecRates,
    #     on_delete=models.CASCADE,
    #     related_name='c2rates_wday'  # Custom related_name for wday_rate
    # )
    # wend_rate = models.ForeignKey(
    #     TimeElecRates,
    #     on_delete=models.CASCADE,
    #     related_name='c2rates_wend'  # Custom related_name for wend_rate
    # )
    class Meta:
        #managed = False
        db_table = 'c2_rates'

# 三段費率表
class C3Rates(models.Model):
    h_id = models.AutoField(primary_key=True, blank=True, null=False)
    #wday_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wday_rate', blank=True, null=False)
    #wend_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wend_rate', blank=True, null=False)
    wday_rate = models.ForeignKey('timeelecrates',  # Use the related model name as a string
    on_delete=models.CASCADE, db_column='wday_rate', related_name='c3rates_wday', to_field='desc',  # Specify the column you want to reference
    )
    wend_rate = models.ForeignKey('timeelecrates',  # Use the related model name as a string
    on_delete=models.CASCADE, db_column='wend_rate', related_name='c3rates_wend', to_field='desc',  # Specify the column you want to reference
    )
    # wday_rate = models.ForeignKey(
    #     TimeElecRates,
    #     on_delete=models.CASCADE,
    #     related_name='c3rates_wday'
    # )
    # wend_rate = models.ForeignKey(
    #     TimeElecRates,
    #     on_delete=models.CASCADE,
    #     related_name='c3rates_wend'
    # )

    class Meta:
        #managed = False
        db_table = 'c3_rates'


# 二段式夏季費率表
class SummerC2Rates(models.Model):
    h_id = models.AutoField(primary_key=True, blank=True, null=False)
    #wday_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wday_rate', blank=True, null=False)
    #wend_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wend_rate', blank=True, null=False)
    wday_rate = models.ForeignKey('timeelecrates',  # Use the related model name as a string
    on_delete=models.CASCADE, db_column='wday_rate', related_name='summerc2rates_wday', to_field='desc',  # Specify the column you want to reference
    )
    wend_rate = models.ForeignKey('timeelecrates',  # Use the related model name as a string
    on_delete=models.CASCADE, db_column='wend_rate', related_name='summerc2rates_wend', to_field='desc',  # Specify the column you want to reference
    )
    # wday_rate = models.ForeignKey(
    #     TimeElecRates,
    #     on_delete=models.CASCADE,
    #     related_name='summerc2rates_wday'
    # )
    # wend_rate = models.ForeignKey(
    #     TimeElecRates,
    #     on_delete=models.CASCADE,
    #     related_name='summerc2rates_wend'
    # )

    class Meta:
        #managed = False
        db_table = 'summer_c2_rates'


# 三段式夏季費率表
class SummerC3Rates(models.Model):
    h_id = models.AutoField(primary_key=True, blank=True, null=False)
    #wday_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wday_rate', blank=True, null=False)
    #wend_rate = models.ForeignKey('TimeElecRates', models.DO_NOTHING, db_column='wend_rate', blank=True, null=False)
    wday_rate = models.ForeignKey('timeelecrates',  # Use the related model name as a string
    on_delete=models.CASCADE, db_column='wday_rate', related_name='summerc3rates_wday', to_field='desc',  # Specify the column you want to reference
    )
    wend_rate = models.ForeignKey('timeelecrates',  # Use the related model name as a string
    on_delete=models.CASCADE, db_column='wend_rate', related_name='summerc3rates_wend', to_field='desc',  # Specify the column you want to reference
    )
    # wday_rate = models.ForeignKey(
    #     TimeElecRates,
    #     on_delete=models.CASCADE,
    #     related_name='summerc3rates_wday'
    # )
    # wend_rate = models.ForeignKey(
    #     TimeElecRates,
    #     on_delete=models.CASCADE,
    #     related_name='summerc3rates_wend'
    # )

    class Meta:
        #managed = False
        db_table = 'summer_c3_rates'




# 交通工具碳當量
class CdeTransport(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        #managed = False
        db_table = 'cde_transport'

    def __str__(self):  
        return self.name

# 碳當量總分類
class CfpClass(models.Model):
    class_id = models.TextField(primary_key=True, blank=True, null=False)
    class_name = models.TextField(blank=True, null=False)

    class Meta:
        #managed = False
        db_table = 'cfp_class'

    def __str__(self):  
        return self.name


class CfpSosClass(models.Model):
    cfp_sos_class_id = models.TextField(primary_key=True, blank=True, null=False)
    cfp_sos_class_name = models.TextField(blank=True, null=False)
    cfp_sub_class = models.ForeignKey('CfpSubClass', models.DO_NOTHING, blank=True, null=False)

    class Meta:
        #managed = False
        db_table = 'cfp_sos_class'


class CfpSubClass(models.Model):
    sub_class_id = models.TextField(primary_key=True, blank=True, null=False)
    sub_class_name = models.TextField(blank=True, null=False)
    class_id = models.ForeignKey(CfpClass, models.DO_NOTHING, db_column='class_id', blank=True, null=False)  # Field renamed because it was a Python reserved word.

    class Meta:
        #managed = False
        db_table = 'cfp_sub_class'


# 蛋類及加工品碳當量
class EggProds(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        #managed = False
        db_table = 'egg_prods'

    def __str__(self):  
        return self.name


# 電器功率表
class ElecDeviceConsumption(models.Model):
    name = models.TextField(unique=True)
    watt = models.IntegerField(blank=True, null=False)
    date = models.DateTimeField(default=timezone.now)  

    class Meta:
        #managed = False
        db_table = 'elec_device_consumption'

    def __str__(self):  
        return self.name


# 能資料碳當量
class Energy(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        #managed = False
        db_table = 'energy'

    def __str__(self):  
        return self.name


# 乳製品碳當量
class LactoseProds(models.Model):
    id = models.TextField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    cde = models.FloatField(blank=True, null=False)
    unit = models.TextField(blank=True, null=False)

    class Meta:
        #managed = False
        db_table = 'lactose_prods'

    def __str__(self):  
        return self.name


