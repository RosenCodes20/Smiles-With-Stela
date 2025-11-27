from django import forms

from mother_gift.cart.models import Addresses


class BaseCartForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = ('first_name', 'last_name', 'address_email', 'town_name', 'speedy_address')

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Моля въведе вашето име", 'id': 'username'}),
            "last_name": forms.TextInput(attrs={"placeholder": "Моля въведе вашата фамилия", 'id': 'username'}),
            "address_email": forms.EmailInput(attrs={"placeholder": "Моля въведете вашия имейл", "id": "username"}),
            "town_name": forms.TextInput(attrs={'placeholder': 'Моля въведете вашия град', 'id': 'username'}),
            'speedy_address': forms.TextInput(attrs={'placeholder': 'Моля въведете адресът на speedy във вашия град', 'id': 'username'})
        }

        labels = {
            "first_name": '',
            "last_name": '',
            "address_email": '',
            'town_name': '',
            'speedy_address': ''
        }

class CreateCartForm(BaseCartForm):
    class Meta(BaseCartForm.Meta):
        pass