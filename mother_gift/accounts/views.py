from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from mother_gift.accounts.forms import UserRegisterForm, EditProfileForm
from mother_gift.accounts.models import Profile

# Create your views here.

UserModel = get_user_model()

class Login(UserPassesTestMixin, LoginView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        elif not self.request.user.is_authenticated:
            return True

    template_name = "login.html"

class Register(UserPassesTestMixin, CreateView):
    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        elif not self.request.user.is_authenticated:
            return True

    template_name = "registration.html"
    model = UserModel
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

class Logout(LogoutView, LoginRequiredMixin):
    template_name = 'logout.html'
    http_method_names = ['post', 'get']


class ProfileDetails(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = UserModel
    template_name = "profile.html"
    context_object_name = "profile"

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user.profile == user.profile


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = "edit-profile.html"
    form_class = EditProfileForm
    context_object_name = "profile"

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user.profile == user.profile

    def get_success_url(self):

        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.object.user.pk
            }
        )