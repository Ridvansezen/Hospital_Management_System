from django.contrib import admin
from doctorsApp.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'experience_years')

admin.site.register(Doctor, DoctorAdmin)
