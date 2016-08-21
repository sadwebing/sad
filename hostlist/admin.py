from django.contrib import admin
from hostlist.models import HostList, Saduser, DataCenter, NetworkOperator, ProvinceArea, Catagory

# Register your models here.

admin.site.register(HostList)
admin.site.register(Saduser)
admin.site.register(DataCenter)
admin.site.register(NetworkOperator)
admin.site.register(ProvinceArea)
admin.site.register(Catagory)
