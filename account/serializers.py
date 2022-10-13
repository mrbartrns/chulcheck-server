from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .validations import validate_username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}, "token": {"read_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user

    # TODO: error 코드 전달하기
    def validate(self, data):
        user = User(**data)
        username = data.get("username")
        password = data.get("password")
        errors = {}

        try:
            validate_username(username=username)
        except ValidationError as e:
            errors["username"] = list(e)

        try:
            validate_password(password=password, user=user)
        except ValidationError as e:
            errors["password"] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return data
