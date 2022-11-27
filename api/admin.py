from django.contrib import admin
from .models import *

# Register your models here.


class AttendenceAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "timestamp"]
    list_display_links = ["id", "user", "timestamp"]


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "leader", "created_at", "updated_at"]
    list_display_links = ["id", "name", "leader"]


admin.site.register(Attendance, AttendenceAdmin)
admin.site.register(Organization, OrganizationAdmin)
