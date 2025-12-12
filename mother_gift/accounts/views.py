from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from mother_gift import settings
from mother_gift.accounts.forms import UserRegisterForm, EditProfileForm, UserForgotPasswordForm
from mother_gift.accounts.models import Profile
from mother_gift.cart.models import OrderUserModel

# Create your views here.

UserModel = get_user_model()

class Login(UserPassesTestMixin, LoginView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        elif not self.request.user.is_authenticated:
            return True

    template_name = "account/login.html"

class Register(UserPassesTestMixin, CreateView):
    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        elif not self.request.user.is_authenticated:
            return True

    template_name = "account/registration.html"
    model = UserModel
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

class Logout(LogoutView, LoginRequiredMixin):
    template_name = 'account/logout.html'
    http_method_names = ['post', 'get']


class ProfileDetails(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = UserModel
    template_name = "account/profile.html"
    context_object_name = "profile"

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user.profile == user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['orders'] = OrderUserModel.objects.filter(user_order=self.request.user)

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = "account/edit-profile.html"
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

def password_reset_view(request):
    form = UserForgotPasswordForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save(
                request=request,
                from_email=settings.DEFAULT_FROM_EMAIL,
                domain_override="127.0.0.1:8000",
            )
            return redirect("password_reset_done")

    context = {
        'form': form,
    }

    return render(request, "registration/password_reset_form.html", context)