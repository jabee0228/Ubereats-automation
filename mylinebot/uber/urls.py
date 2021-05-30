from django.urls import path,include
from . import views

urlpatterns = [
    path('callback', views.callback)
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uber/', include('uber.urls'))  # 包含應用程式的網址
]