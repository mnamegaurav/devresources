from django.urls import path
from django.contrib.auth.decorators import login_required

from core.views import (
    HomeView,
    AboutView,
    ContactView,
    ResourceListByCategoryView,
    ResourceListAddedByUserView,
    ResourceCreateView,
    ResourceUpdateView,
    ResourceDeleteView,
    GitHubGistListByCategoryView,
    GitHubGistListAddedByUserView,
    GitHubGistCreateView,
    GitHubGistUpdateView,
    GitHubGistDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home_view"),
    path("about/", AboutView.as_view(), name="about_view"),
    path("contact/", ContactView.as_view(), name="contact_view"),
    path(
        "category/resources/<str:category_slug>/",
        ResourceListByCategoryView.as_view(),
        name="resource_list_view",
    ),
    path(
        "category/gists/<str:category_slug>/",
        GitHubGistListByCategoryView.as_view(),
        name="github_gist_list_view",
    ),
    # URls for only authenticated users
    path(
        "resource/list/",
        login_required(ResourceListAddedByUserView.as_view()),
        name="resource_list_by_me_view",
    ),
    path(
        "resource/create/",
        login_required(ResourceCreateView.as_view()),
        name="resource_create_view",
    ),
    path(
        "resource/update/<int:pk>/",
        login_required(ResourceUpdateView.as_view()),
        name="resource_update_view",
    ),
    path(
        "resource/delete/<int:pk>/",
        login_required(ResourceDeleteView.as_view()),
        name="resource_delete_view",
    ),
    path(
        "gist/list/",
        login_required(GitHubGistListAddedByUserView.as_view()),
        name="github_gist_list_by_me_view",
    ),
    path(
        "gist/create/",
        login_required(GitHubGistCreateView.as_view()),
        name="github_gist_create_view",
    ),
    path(
        "gist/update/<int:pk>/",
        login_required(GitHubGistUpdateView.as_view()),
        name="github_gist_update_view",
    ),
    path(
        "gist/delete/<int:pk>/",
        login_required(GitHubGistDeleteView.as_view()),
        name="github_gist_delete_view",
    ),
]
