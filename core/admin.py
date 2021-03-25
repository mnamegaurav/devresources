from django.contrib import admin
from core.models import (
    ResourceCategory,
    Resource,
    ContactUs,
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
    prepopulated_fields = {"slug": ("title",)}
    


@admin.register(Resource)
class ResourceModelAdmin(admin.ModelAdmin):
    model = Resource
    filter_horizontal = ('category',)
    list_display = (
        'title',
        'url',
        'is_active',
        'added_on',
        'updated_on',
        'added_by',
        'updated_by',
        )
    list_filter = ('is_active', 'category', 'added_by', 'updated_by')
    search_fields = ('title',)



@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = (
        'full_name',
        'email',
        'message',
        'added_on',
        )