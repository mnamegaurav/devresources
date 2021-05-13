from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from django.utils.translation import gettext as _

from hitcount.models import HitCountMixin, HitCount

from core.utils import auto_save_current_user

# Current User Model
User = get_user_model()


class ResourceCategory(models.Model):
    title = models.CharField(max_length=140, verbose_name=_("Title"))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_("Slug"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active?"))
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Added By"),
    )
    hit_count = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Resource Category"
        verbose_name_plural = "Resource Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super().save(*args, **kwargs)

    def first_letter(self):
        return self.title[0]


class Resource(models.Model):
    title = models.CharField(max_length=140, verbose_name=_("Title"))
    # thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    # description = models.CharField(max_length=240, null=True, blank=True)
    url = models.URLField(max_length=500, verbose_name=_("Resource Link"))
    category = models.ManyToManyField(
        ResourceCategory, verbose_name=_("Resource Category")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Active?"))
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(
        User,
        related_name="resource_cb",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Added By"),
    )
    updated_by = models.ForeignKey(
        User,
        related_name="resource_ub",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Updated By"),
    )

    class Meta:
        ordering = ["-updated_on"]
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super().save(*args, **kwargs)

    def first_letter(self):
        return self.title[0]


class CodeSnippet(models.Model):
    title = models.CharField(max_length=140, verbose_name=_("Title"))
    category = models.ManyToManyField(
        ResourceCategory, verbose_name=_("Resource Category")
    )
    code = models.TextField(verbose_name=_("Code Snippet"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active?"))
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(
        User,
        related_name="code_snippet_cb",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Added By"),
    )
    updated_by = models.ForeignKey(
        User,
        related_name="code_snippet_ub",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Updated By"),
    )

    class Meta:
        ordering = ["-updated_on"]
        verbose_name = "Code Snippet"
        verbose_name_plural = "Code Snippets"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super().save(*args, **kwargs)


class ContactUs(models.Model):
    full_name = models.CharField(max_length=140, verbose_name=_("Your Full Name"))
    email = models.EmailField(verbose_name=_("Your Email"))
    message = models.CharField(
        max_length=255, verbose_name=_("Write somethig to us...")
    )
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_on"]
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.full_name
