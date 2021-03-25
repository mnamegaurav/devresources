from urllib import parse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View, TemplateView
from django.views.generic.edit import (
    CreateView, 
    UpdateView, 
    )
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator

from ratelimit.decorators import ratelimit

from hitcount.views import HitCountMixin
from hitcount.models import HitCount

from core.models import (
    ResourceCategory,
    Resource,
    )
from core.forms import ResourceForm, ContactUsForm


class HomeView(View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        all_resource_categories = ResourceCategory.objects.filter(is_active=True)
        
        # filtering the resource categories by hit count and is_active field
        top_resource_categories = ResourceCategory.objects.filter(
                is_active=True
            ).order_by(
                '-hit_count__hits'
            )[:3]

        parsed_website_url = parse.urlparse(request.build_absolute_uri('/'))

        context = {
            'all_resource_categories': all_resource_categories,
            'top_resource_categories': top_resource_categories,
            'hostname': f'{parsed_website_url.hostname}{parsed_website_url.path}'
        }

        return render(request, self.template_name, context)


class ResourceListByCategoryView(View, HitCountMixin):
    template_name = 'core/resource_list.html'
    url_kwarg = 'category_slug'
    
    def get(self, request, *args, **kwargs):
        category_slug = kwargs.get(self.url_kwarg)

        # Counting the number of hits on resource categories
        try:
            resource_category = ResourceCategory.objects.get(slug=category_slug)
            hit_count_obj = HitCount.objects.get_for_object(resource_category)
            hit_count_response = self.hit_count(request, hit_count_obj)
        except Exception as e:
            print('Error: ', e)

        # filtering the resources by is_active and current url slug
        all_resources = Resource.objects.filter(
            is_active=True,
            category__slug=category_slug
            )

        context = {
            'all_resources': all_resources,
            'category_slug': category_slug,
        }

        return render(request, self.template_name, context)


class ResourceListAddedByUserView(View):
    template_name = 'core/resource_list_added_by_user.html'
    url_kwarg = 'tag'

    def get(self, request, *args, **kwargs):
        category = request.GET.get(self.url_kwarg)

        if category:
            # filtering the resources by current user
            all_resources = Resource.objects.filter(
                added_by=request.user,
                category__slug=category,
                is_active=True
                )
        else:
            # filtering the resources by current user
            all_resources = Resource.objects.filter(
                added_by=request.user,
                is_active=True
                )

        context = {
            'all_resources': all_resources,
        }

        return render(request, self.template_name, context)


class ResourceCreateView(SuccessMessageMixin, CreateView):
    template_name = 'core/resource_create_form.html'
    success_message = "Successfully added"
    success_url = reverse_lazy('resource_list_by_me_view')
    form_class = ResourceForm


class ResourceUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'core/resource_update_form.html'
    success_message = "Successfully updated"
    success_url = reverse_lazy('resource_list_by_me_view')
    form_class = ResourceForm

    def get_queryset(self):
        queryset = Resource.objects.filter(added_by=self.request.user)
        return queryset


class ResourceDeleteView(View):
    success_message = "Successfully deleted"
    success_url = reverse_lazy('resource_list_by_me_view')

    def post(self, request, *args, **kwargs):
        resource_pk = kwargs.get('pk')

        try:
            resource_obj = Resource.objects.get(pk=resource_pk)
            resource_obj.is_active = False
            resource_obj.save()
            messages.success(request, self.success_message, extra_tags="success")
        except Exception as e:
            pass
        
        return redirect(self.success_url)



class AboutUsView(TemplateView):
    template_name = 'about.html'
    

@method_decorator(ratelimit(key='ip', rate='1/d', method=ratelimit.UNSAFE), name='post')
class ContactUsView(SuccessMessageMixin, CreateView):
    template_name = 'contact_us.html'
    success_message = "Thanks for contcting Us, We will get back to you soon."
    success_url = reverse_lazy('contact_us_view')
    form_class = ContactUsForm