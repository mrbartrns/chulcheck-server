from rest_framework import serializers
from .models import *
from account.serializers import UserSerializer


class AttendenceSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ("id", "user", "timestamp")
