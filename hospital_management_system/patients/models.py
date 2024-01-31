from django.db import models
from doctorsApp.models import Doctor

class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15,)
    address = models.TextField(blank=True, null=True)
    blood_type = models.CharField(max_length=5, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    policy_number = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.appointment_date} {self.appointment_time}"
