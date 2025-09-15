from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from mother_gift.accounts.models import User

UserModel = get_user_model()

class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("email",)

        labels = {
            'email': 'Имейл',
            'password': 'Парола'
        }

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Въведи твоят имейл'}),
            'password': forms.TextInput(attrs={'placeholder': 'Въведи твоята парола'})
        }


class AppUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UserModel

