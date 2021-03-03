from django.urls import path, include
# from django.urls import reverse_lazy
from django.contrib.auth.views import (
    
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
    )

from accounts.views import (
    SignInView,
    SignUpView,
    )


urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
]
