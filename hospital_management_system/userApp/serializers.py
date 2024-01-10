from .models import UserModel
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator

User = UserModel

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, validators=[MinLengthValidator(limit_value=8), MaxLengthValidator(limit_value=24)])

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email', 'gender', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data.get('phone_number', None),
            email=validated_data['email'],
            gender=validated_data.get('gender', 'other'),
            password=validated_data['password'],
        )
        return user