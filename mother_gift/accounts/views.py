from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.

UserModel = get_user_model()

class Login(LoginView):

    template_name = "login.html"

def register(request):
    return render(request, 'registration.html')