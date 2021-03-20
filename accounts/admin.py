from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
    )
# Register your models here.

User = get_user_model()

# ModelAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('website',)}),
        )
    fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('website',)}),
        )