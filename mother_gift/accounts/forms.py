from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from mother_gift.accounts.models import User, Profile

UserModel = get_user_model()

class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("email",)

        labels = {
            'email': 'Имейл',
            'password1': 'Парола',
            'password2': 'Потвърди паролата'
        }

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Въведи твоят имейл', "id": "username"}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Въведи твоята парола', "id": "username"}),
            'password2': forms.TextInput(attrs={'placeholder': 'Въведи твоята парола отново', "id": "username"})
        }


class AppUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UserModel


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')

        labels = {
            'first_name': 'Първо Име',
            'last_name': 'Фамилия',
            'profile_picture': 'Профилна снимка'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Моля въведете първо име', 'id': 'username'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Моля въведете фамилия', 'id': 'username'}),
        }

class UserForgotPasswordForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ("email",)
