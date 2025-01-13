from django.contrib.auth.models import User
# use django authenticate method to authenticate user
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def validate(self, data):
        if User.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError('Email already exists')
        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError('Username already exists')
        # password validation
        if len(data.get('password')) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        if data.get('password').isalpha():
            raise serializers.ValidationError('Password must contain at least one number')
        if data.get('password').isdigit():
            raise serializers.ValidationError('Password must contain at least one letter')
        if data.get('password').islower():
            raise serializers.ValidationError('Password must contain at least one uppercase letter')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        return user


class TokenPairObtainSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is None:
            raise serializers.ValidationError('Invalid username or password')
        return user

class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        refresh = data.get('refresh')
        if not refresh:
            raise serializers.ValidationError('Invalid refresh token')
        try:
            refresh = RefreshToken(refresh)
        except TokenError:
            raise serializers.ValidationError('Invalid refresh token')
        return refresh

