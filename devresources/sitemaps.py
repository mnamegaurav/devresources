from django.contrib import sitemaps
from django.urls import reverse_lazy, reverse
from core.models import (
    ResourceCategory,
    Resource
    )


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['about_view', 'contact_view',]

    def location(self, obj):
        return reverse(obj)


# class ResourceSitemap(sitemaps.Sitemap):
#     priority = 1
#     changefreq = 'hourly'

#     def items(self):
#         return Resource.objects.filter(is_active=True)

#     def location(self, obj):
#         return obj.url

#     def lastmod(self, obj):
#         return obj.updated_on


class ResourceCategorySitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'weekly'

    def items(self):
        return ResourceCategory.objects.filter(is_active=True)

    def location(self, obj):
        return reverse('resource_list_view', kwargs={'category_slug': obj.slug})

    def lastmod(self, obj):
        return obj.updated_on