from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView

from users.forms import CustomSignUpForm, CustomLoginForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm


# Create your views here.

class CustomSignUpView(generic.CreateView):
    form_class = CustomSignUpForm #We're subclassing the generic class-based view CreateView in our SignUp class. We specify using the built-in UserCreationForm
    success_url = reverse_lazy("home") #to redirect the user to the home page upon successful registration.
    template_name = "registration/signup.html"

    # To autologin after successful signup
    def form_valid(self, form):
        valid = super(CustomSignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = form.save()
        login(self.request, user)
        return valid

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy("home")
    template_name: str = "registration/login.html"

# def logout_view(request):
#     logout(request)

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    # redirect_authenticated_user: bool = True
    success_url = reverse_lazy("password_reset_done")
    template_name: str = "registration/password_reset.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    success_url = reverse_lazy("password_reset_complete")
    template_name: str = "registration/password_reset_confirm.html"