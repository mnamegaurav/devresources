from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import (
    authenticate, 
    login, logout, 
    get_user_model,
    )

from accounts.forms import (
    CustomUserCreatationForm, 
    CustomUserChangeForm
    )
# Create your views here.
User = get_user_model()


class SignInView(View):
    template_name = 'accounts/signin.html'
    success_message = "Whoa! You are inside"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')  

        user = authenticate(request, email=email, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Login.', extra_tags="danger")
            return render(request, self.template_name) 

        login(request, user)
        messages.success(request, self.success_message, extra_tags="success")
        return redirect('/')
        


class SignUpView(View):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreatationForm
    success_message = "Almost there, put your email and password here"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, self.success_message, extra_tags="success")
            return redirect('signin_view')

        messages.error(request, 'Something is missing, try again', extra_tags="danger")
        context = {'form': form}
        return render(request, self.template_name, context)


class SignOutView(View):
    success_message = "See you soon."

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, self.success_message, extra_tags="success")
        return redirect('/')


class ProfileView(View):
    template_name = 'accounts/profile.html'
    success_message = 'Successfully saved the profile.'
    form_class = CustomUserChangeForm

    def get(self, request, *args, **kwargs):

        form = self.form_class(instance=request.user)
        context = {'form': form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        # save the profile data
        form = self.form_class(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, self.success_message, extra_tags="success")
            return redirect('profile_view')
        else:
            messages.error(request, 'Please recheck all the details.', extra_tags="danger")
            context = {'form': form}
            return render(request, self.template_name, context)