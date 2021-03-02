from django.contrib import admin
from core.models import (
    ResourceCategory,
    Resource
)


@admin.register(ResourceCategory)
class ResourceCategoryModelAdmin(admin.ModelAdmin):
    model = ResourceCategory
    list_display = (
        'title', 
        'slug',
        'is_active', 
        'added_on', 
        'updated_on', 
        'added_by',
        )


@admin.register(Resource)
class ResourceModelAdmin(admin.ModelAdmin):
    model = Resource
    filter_horizontal = ('category',)
    list_display = (
        'title',
        'thumbnail',
        'description',
        'url',
        'is_active',
        'added_on',
        'updated_on',
        'added_by',
        )