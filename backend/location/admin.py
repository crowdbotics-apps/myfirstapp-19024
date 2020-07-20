from django.contrib import admin
from .models import TaskLocation, CustomerLocation, TaskerLocation, MapLocation

admin.site.register(TaskerLocation)
admin.site.register(MapLocation)
admin.site.register(CustomerLocation)
admin.site.register(TaskLocation)

# Register your models here.
