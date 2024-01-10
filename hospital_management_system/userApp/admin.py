from django.contrib import admin
from userApp.models import UserModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'gender')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'gender')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    list_display = ('id', 'username', 'first_name', 'last_name', 'gender', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name',)
    list_filter = ('gender', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('id',)

admin.site.register(UserModel, CustomUserAdmin)
