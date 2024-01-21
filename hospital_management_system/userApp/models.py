from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


class UserModel(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,
                              default='other')

    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission,
                                              related_name='user_permissions')
    

    
