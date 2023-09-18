from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, ElecDeviceConsumption, Beverage

# admin.site.register(Post) #告訴manage 把 model的post 列入管理
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

admin.site.register(Post, PostAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'watt')

admin.site.register(ElecDeviceConsumption, DeviceAdmin)

class BeverageAdmin(admin.ModelAdmin):
    list_display = ('name', 'cde')

admin.site.register(Beverage, BeverageAdmin)