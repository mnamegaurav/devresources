from django.urls import path, include
from accounts.views import (
    SignInView,
    SignOutView,
    SignUpView,
    )


urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
]
