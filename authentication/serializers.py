from rest_framework import serializers
from .models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            "username",
            "email",
            "is_prime_member",
            "is_premium_member",
            "age",
            "country",
        ]

    def create(self, validated_data):
        user = AppUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        user.dob = validated_data["dob"]
        user.country = validated_data["country"]
        user.save()
        return user
