from django.urls import path, include
from django.contrib.auth.decorators import login_required
from accounts.views import (
    SignInView,
    SignOutView,
    SignUpView,
    ProfileView,
    )


urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin_view'),
    path('signout/', login_required(SignOutView.as_view()), name='signout_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('profile/', login_required(ProfileView.as_view()), name='profile_view'),
]
