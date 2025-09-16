from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mother_gift.accounts.forms import UserRegisterForm

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
