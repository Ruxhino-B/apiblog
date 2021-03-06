from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'email', 'password')
        model = CustomUser
