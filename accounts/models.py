from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Optional fields
    full_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
