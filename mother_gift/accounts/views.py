from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.

UserModel = get_user_model()

class Login(UserPassesTestMixin, LoginView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        elif not self.request.user.is_authenticated:
            return True

    template_name = "login.html"

def register(request):
    return render(request, 'registration.html')