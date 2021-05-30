from django.urls import path,include
from . import views


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uber/', include('uber.urls')),
    path('callback', views.callback)# 包含應用程式的網址
]