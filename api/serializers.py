from rest_framework import serializers
from .models import *


class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = {"id", "user", "timestamp"}
