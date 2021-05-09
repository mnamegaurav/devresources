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

from hitcount.views import HitCountMixin
from hitcount.models import HitCount

from core.models import (
    ResourceCategory,
    Resource,
    GitHubGist,
)
from core.forms import ResourceForm, GitHubGistForm, ContactForm


class HomeView(View):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        all_resource_categories = ResourceCategory.objects.filter(is_active=True)

        # filtering the resource categories by hit count and is_active field
        top_resource_categories = ResourceCategory.objects.filter(
            is_active=True
        ).order_by("-hit_count__hits")[:3]

        parsed_website_url = parse.urlparse(request.build_absolute_uri("/"))

        if request.user.is_authenticated:
            page_title = "Home"
        else:
            page_title = "One destination for all the developer's learning resources."

        context = {
            "all_resource_categories": all_resource_categories,
            "top_resource_categories": top_resource_categories,
            "hostname": f"{parsed_website_url.hostname}{parsed_website_url.path}",
            "page_title": page_title,
        }

        return render(request, self.template_name, context)


class ResourceListByCategoryView(View, HitCountMixin):
    template_name = "core/resource_list.html"
    url_kwarg = "category_slug"

    def get(self, request, *args, **kwargs):
        category_slug = kwargs.get(self.url_kwarg)

        # Counting the number of hits on resource categories
        try:
            resource_category = ResourceCategory.objects.get(slug=category_slug)
            hit_count_obj = HitCount.objects.get_for_object(resource_category)
            hit_count_response = self.hit_count(request, hit_count_obj)
        except Exception as e:
            print("Error: ", e)

        # filtering the resources by is_active and current url slug
        all_resources = Resource.objects.filter(
            is_active=True, category__slug=category_slug
        )

        context = {
            "all_resources": all_resources,
            "category_slug": category_slug,
            "page_title": category_slug.capitalize(),
        }

        return render(request, self.template_name, context)


class ResourceListAddedByUserView(View):
    template_name = "core/resource_list_added_by_user.html"
    url_kwarg = "tag"
    page_title = "My Resources"

    def get(self, request, *args, **kwargs):
        category = request.GET.get(self.url_kwarg)

        if category:
            # filtering the resources by current user
            all_resources = Resource.objects.filter(
                added_by=request.user, category__slug=category, is_active=True
            )
        else:
            # filtering the resources by current user
            all_resources = Resource.objects.filter(
                added_by=request.user, is_active=True
            )

        context = {"all_resources": all_resources, "page_title": self.page_title}

        return render(request, self.template_name, context)


class ResourceCreateView(SuccessMessageMixin, CreateView):
    template_name = "core/resource_create_form.html"
    success_message = "Successfully added"
    success_url = reverse_lazy("resource_list_by_me_view")
    form_class = ResourceForm
    extra_context = {"page_title": "Create A New Resource"}


class ResourceUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "core/resource_update_form.html"
    success_message = "Successfully updated"
    success_url = reverse_lazy("resource_list_by_me_view")
    form_class = ResourceForm
    extra_context = {"page_title": "Update Resource"}

    def get_queryset(self):
        queryset = Resource.objects.filter(added_by=self.request.user)
        return queryset


class ResourceDeleteView(View):
    success_message = "Successfully deleted"
    success_url = reverse_lazy("resource_list_by_me_view")

    def post(self, request, *args, **kwargs):
        resource_pk = kwargs.get("pk")

        try:
            resource_obj = Resource.objects.get(pk=resource_pk)
            resource_obj.is_active = False
            resource_obj.save()
            messages.success(request, self.success_message, extra_tags="success")
        except Exception as e:
            pass

        return redirect(self.success_url)


class GitHubGistListByCategoryView(View, HitCountMixin):
    template_name = "core/github_gist_list.html"
    url_kwarg = "category_slug"

    def get(self, request, *args, **kwargs):
        category_slug = kwargs.get(self.url_kwarg)

        # Counting the number of hits on resource categories
        try:
            resource_category = ResourceCategory.objects.get(slug=category_slug)
            hit_count_obj = HitCount.objects.get_for_object(resource_category)
            hit_count_response = self.hit_count(request, hit_count_obj)
        except Exception as e:
            print("Error: ", e)

        # filtering the resources by is_active and current url slug
        all_github_gists = GitHubGist.objects.filter(
            is_active=True, category__slug=category_slug
        )

        context = {
            "all_github_gists": all_github_gists,
            "category_slug": category_slug,
            "page_title": category_slug.capitalize(),
        }

        return render(request, self.template_name, context)


class GitHubGistListAddedByUserView(View):
    template_name = "core/github_gist_list_added_by_user.html"
    url_kwarg = "tag"
    page_title = "My GitHub Gists"

    def get(self, request, *args, **kwargs):
        category = request.GET.get(self.url_kwarg)

        if category:
            # filtering the resources by current user
            all_github_gists = GitHubGist.objects.filter(
                added_by=request.user, category__slug=category, is_active=True
            )
        else:
            # filtering the resources by current user
            all_github_gists = GitHubGist.objects.filter(
                added_by=request.user, is_active=True
            )

        context = {"all_github_gists": all_github_gists, "page_title": self.page_title}

        return render(request, self.template_name, context)


class GitHubGistCreateView(SuccessMessageMixin, CreateView):
    template_name = "core/github_gist_create_form.html"
    success_message = "Successfully added"
    success_url = reverse_lazy("github_gist_list_by_me_view")
    form_class = GitHubGistForm
    extra_context = {"page_title": "Create A New GitHub Gist"}


class GitHubGistUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "core/github_gist_update_form.html"
    success_message = "Successfully updated"
    success_url = reverse_lazy("github_gist_list_by_me_view")
    form_class = GitHubGistForm
    extra_context = {"page_title": "Update GitHub Gist"}

    def get_queryset(self):
        queryset = GitHubGist.objects.filter(added_by=self.request.user)
        return queryset


class GitHubGistDeleteView(View):
    success_message = "Successfully deleted"
    success_url = reverse_lazy("github_gist_list_by_me_view")

    def post(self, request, *args, **kwargs):
        github_gist_pk = kwargs.get("pk")

        try:
            github_gist_obj = GitHubGist.objects.get(pk=github_gist_pk)
            github_gist_obj.is_active = False
            github_gist_obj.save()
            messages.success(request, self.success_message, extra_tags="success")
        except Exception as e:
            pass

        return redirect(self.success_url)


class AboutView(TemplateView):
    template_name = "about.html"
    extra_context = {"page_title": "About Us"}


class ContactView(SuccessMessageMixin, CreateView):
    template_name = "contact.html"
    success_message = "Thanks for contacting us, We will get back to you soon."
    success_url = reverse_lazy("contact_view")
    form_class = ContactForm
    extra_context = {"page_title": "Contact Us"}
