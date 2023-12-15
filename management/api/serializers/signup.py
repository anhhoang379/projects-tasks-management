from django.contrib.auth.models import User
from rest_framework import serializers

from management.models import Staff


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ("username", "password")


class SignUpSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    confirm_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = Staff
        fields = [
            "user",
            "confirm_password",
            "role",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        password = user_data.pop("password")
        confirm_password = validated_data.pop("confirm_password")
        role = validated_data.pop("role")

        if password != confirm_password:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match"}
            )

        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()

        staff = Staff.objects.create(user=user, role=role)

        return staff
