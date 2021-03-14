from django.urls import path
from django.contrib.auth.decorators import login_required
from core.views import (
    HomeView,
    ResourceListByCategoryView,
    ResourceListAddedByUserView,
    ResourceCreateView,
    ResourceUpdateView,
    ResourceDeleteView,
    )

urlpatterns = [
    path(
        '', 
        HomeView.as_view(),
        name='home_view'
        ),
    path(
        'cat/<str:category_slug>/', 
        ResourceListByCategoryView.as_view(),
        name='resource_list_view'
        ),

    # URls for only authenticated users
    path(
        'resource/list/', 
        login_required(ResourceListAddedByUserView.as_view()),
        name='resource_list_by_me_view'
        ),
    path(
        'resource/create/', 
        login_required(ResourceCreateView.as_view()),
        name='resource_create_view'
        ),
    path(
        'resource/update/<int:pk>/', 
        login_required(ResourceUpdateView.as_view()),
        name='resource_update_view'
        ),
    path(
        'resource/delete/<int:pk>/',
        login_required(ResourceDeleteView.as_view()),
        name='resource_delete_view'
        ),
]
