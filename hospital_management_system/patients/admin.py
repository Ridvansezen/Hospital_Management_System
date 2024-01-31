from django.contrib import admin
from patients.models import Patient
from patients.models import Appointment

class CustomPatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'gender', 'blood_type',)
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('gender', 'blood_type',)

admin.site.register(Patient, CustomPatientAdmin)




admin.site.register(Appointment)