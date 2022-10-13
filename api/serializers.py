from rest_framework import serializers
from .models import *


class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("id", "user", "timestamp")
