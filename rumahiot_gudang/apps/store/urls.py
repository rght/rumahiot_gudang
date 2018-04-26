# from django.contrib import admin
from django.conf.urls import url

from rumahiot_gudang.apps.store.views import store_device_data, store_new_device, store_new_device

urlpatterns = [
    url(r'^device/data$', store_device_data, name='store_device_data'),
    url(r'^device/new$', store_new_device, name='store_new_device')
]
