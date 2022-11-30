from rest_framework import serializers
from .models import *
from account.serializers import UserSerializer


class AttendenceSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ("id", "user", "timestamp")


class OrganizationSerializer(serializers.ModelSerializer):

    leader = UserSerializer(read_only=True)
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Organization
        fields = ("id", "name", "leader", "members", "created_at", "updated_at")
