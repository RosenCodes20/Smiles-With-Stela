from django import forms

from mother_gift.cart.models import Addresses


class BaseCartForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = ('first_name', 'last_name', 'address_email', 'town_name', 'speedy_address')

        widgets = {
            "town_name": forms.TextInput(attrs={'placeholder': 'Моля въведете вашия град', 'id': 'username'}),
            'speedy_address': forms.TextInput(attrs={'placeholder': 'Моля въведете адресът на speedy във вашия град', 'id': 'username'})
        }

        labels = {
            'town_name': '',
            'speedy_address': ''
        }

class CreateCartForm(BaseCartForm):
    class Meta(BaseCartForm.Meta):
        pass