from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify

from hitcount.models import HitCountMixin, HitCount

from core.utils import auto_save_current_user

# Current User Model
User = get_user_model()


class ResourceCategory(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        null=True, blank=True,
        editable=False
        )
    hit_count = GenericRelation(
        HitCount, 
        object_id_field='object_pk', 
        related_query_name='hit_count_generic_relation'
        )

    class Meta:
        ordering = ['title']
        verbose_name = 'Resource Category'
        verbose_name_plural = 'Resource Categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(ResourceCategory, self).save(*args, **kwargs)

    def first_letter(self):
        return self.title[0]


class Resource(models.Model):
    title = models.CharField(max_length=140)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    description = models.CharField(max_length=240, null=True, blank=True)
    url = models.URLField(max_length=500)
    category = models.ManyToManyField(ResourceCategory)
    is_active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        null=True, blank=True,
        editable=False
        )

    class Meta:
        ordering = ['-updated_on']
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Resource, self).save(*args, **kwargs)

    def first_letter(self):
        return self.title[0]