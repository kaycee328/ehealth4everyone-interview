from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True
    )  # write_only ensures password isn’t exposed

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            # Authenticate user
            user = authenticate(username=username, password=password)
            if user:
                data["user"] = user  # Pass the user in the validated data
            else:
                raise serializers.ValidationError("Invalid login credentials.")
        else:
            raise serializers.ValidationError("Username and password are required.")

        return data
