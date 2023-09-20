"""
URL configuration for mblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#原始檔開始
#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
#    path("admin/", admin.site.urls),
#]
#原始結束

from django.contrib import admin
from django.urls import path
from mainsite.views import *     #從mainsite資料夾引入homepage
from api.views import *                    # 0913 

urlpatterns = [                         #陣列型式,每筆資料中間要用','
    path('admin/', admin.site.urls),    #(路徑, 顥示函數 def ...)
    #path('',homepage),                   #空字串, 方法為 homepage
    path('', index_post),                     # 因為建立 index了, 所以取代 homepage
    path('post/<slug:slug>', showpost),  #08/07新增 將<slug:slug>傳到 showpost這個view
    path("api/", test),                  #09/13 新增 api的app
    path('api/doc/', apiTestView),
    path('api/power/', calculate_electricity_cost_view),
    path('api/devices/', showdevice),
    path('pages/query/', customSqlQueryView),
    path('api/power/accu_usage', calculate_accumulative_usage_view),
    path('api/power/accu_cost',calculate_accumulative_cost_view),
    path('api/cde/',calculate_cde_View),
    path('index2/', index2_post),
    path('index3/', index3_post),
    path('index4/', index4_post),
    path('index5/', index5_post),
    path('index6/', index6_post),
    path('post/<str:slug>', showpost),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import mblog.settings
if mblog.settings.DEBUG:    #當true會進到runserver模式
    urlpatterns += staticfiles_urlpatterns()