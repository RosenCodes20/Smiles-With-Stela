from django import forms

from mother_gift.cart.models import Addresses


class BaseCartForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = "__all__"

        widgets = {
            "town_name": forms.TextInput(attrs={'placeholder': 'Моля въведете името на вашия град'}),
            'speedy_address': forms.TextInput(attrs={'placeholder': 'Моля въведете адресът на speedy във вашия град'})
        }