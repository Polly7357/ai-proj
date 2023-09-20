from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# admin.site.register(Post) #告訴manage 把 model的post 列入管理
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

admin.site.register(Post, PostAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'watt')

admin.site.register(ElecDeviceConsumption, DeviceAdmin)

class BeverageAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'cde')
    search_fields = ['name'] 

admin.site.register(Beverage, BeverageAdmin)

class TransportAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'cde', 'unit')

admin.site.register(CdeTransport, TransportAdmin)

class CfpClassAdmin(admin.ModelAdmin):
    list_display = ('class_id','class_name')

admin.site.register(CfpClass, CfpClassAdmin)

class EnergyAdmin(admin.ModelAdmin):
    list_display = ('id','name','cde')
    search_fields = ['id','name']

admin.site.register(Energy, EnergyAdmin)


class LactoseProdsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'cde')

admin.site.register(LactoseProds, LactoseProdsAdmin)


class EggProdsProdsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'cde')

admin.site.register(EggProds, EggProdsProdsAdmin)
