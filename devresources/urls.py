"""devresources URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap

from devresources.sitemaps import (
    StaticViewSitemap,
    ResourceCategorySitemap,
    )

sitemap_arg = {
    'sitemaps': {
        'static': StaticViewSitemap,
        'resource_categories': ResourceCategorySitemap,
    }
}

urlpatterns = [
    path('devjunction/devresources/gaurav/admin/', admin.site.urls),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt", 
            content_type="text/plain"
        ),
    ),
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),

    path(
        'sitemap.xml', 
        sitemap, 
        sitemap_arg, 
        name='django.contrib.sitemaps.views.sitemap'
        )
]

if settings.DEBUG:
    urlpatterns.extend(
        static(
            settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT
            )
        )
