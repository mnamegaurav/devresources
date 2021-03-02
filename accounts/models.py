from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Optional fields
    full_name = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    def __str__(self):
        return self.username