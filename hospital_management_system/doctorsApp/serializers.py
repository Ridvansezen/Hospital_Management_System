from doctorsApp.models import Doctor
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'