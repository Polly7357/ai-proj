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
from mainsite.views import homepage, index     #從mainsite資料夾引入homepage

urlpatterns = [                         #陣列型式,每筆資料中間要用','
    path('admin/', admin.site.urls),    #(路徑, 顥示函數 def ...)
    #path('',homepage)                   #空字串, 方法為 homepage
    path("", index)                     # 因為建立 index了, 所以取代 homepage
]
