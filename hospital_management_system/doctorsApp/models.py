from django.db import models
from django.core.validators import MinLengthValidator

class Doctor(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    specialization = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        validators=[MinLengthValidator(10)]
        )
    experience_years = models.IntegerField()
    
    def __str__(self):
        return self.name
