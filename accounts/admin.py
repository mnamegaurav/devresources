from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import (
    CustomUserCreatationForm, 
    CustomUserChangeForm
    )
# Register your models here.

User = get_user_model()

# ModelAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreatationForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('about', 'website')}),
        )
    fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('about', 'website')}),
        )