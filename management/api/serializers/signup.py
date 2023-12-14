import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from management.models import User


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=250, label="username")
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "confirm_password",
            "role",
        ]

    def validate_username(self, username):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if not re.fullmatch(regex, username):
            raise serializers.ValidationError("Invalid Username")
        if User.objects.check_username(username):
            raise serializers.ValidationError("User is exists.")
        return username

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Password does not match.")
        return attrs

    def create(self, validated_data):
        username = validated_data["username"]
        email = (validated_data["email"],)
        password = validated_data["password"]
        role = validated_data["role"]
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
            is_active=True,
        )

        return user
