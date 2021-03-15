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

    # Number of resources count added by a user
    @property
    def added_resource_count(self):
        return self.resource_cb.count()

    # Number of resource categiry view count added by a user
    @property
    def added_resource_category_view_count(self):
        """
        Count the sum of total views(hits) in each category to which a user has added a resource.
        Let's say a user has added 5 resources on java, python and web development categories,
        not java and python and webdevelopment each has 10, 20 and 30 total hits respectively, 
        so this property will return 60(=10+20+30).
        """
        count = 'N/A'
        return count
    