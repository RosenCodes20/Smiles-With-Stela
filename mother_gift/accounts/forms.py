from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
            'email': forms.TextInput(attrs={'placeholder': 'Въведи твоят имейл'}),
            'id_password1': forms.TextInput(attrs={'placeholder': 'Въведи твоята парола'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Въведи твоята парола отново'})
        }


class AppUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UserModel


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')