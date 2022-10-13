from django.contrib import admin
from .models import *

# Register your models here.


class AttendenceAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "timestamp"]
    list_display_links = ["id", "user", "timestamp"]


admin.site.register(Attendance, AttendenceAdmin)
