from django import forms


class SearchForm(forms.Form):
    product = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Моля въведете продукт за търсене..'}
        )
    )