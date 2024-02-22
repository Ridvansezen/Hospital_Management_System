from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator
from patients.models import Patient
from patients.models import Appointment
from doctorsApp.models import Doctor
from doctorsApp.serializers import DoctorSerializer

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        
        
class PatientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name','last_name'] 

class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["name", "specialization"]

class AppointmentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), write_only=True)
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), write_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'appointment_date', 'appointment_time', 'created_at']
        
        
class CustomAppointmentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    patient_name = serializers.SerializerMethodField(read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    doctor_specialization = serializers.CharField(source="doctor.specialization", read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient_name', 'doctor_name',"doctor_specialization" , 'appointment_date', 'appointment_time', 'created_at']

    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"