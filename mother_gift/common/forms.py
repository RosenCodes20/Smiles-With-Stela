from django import forms


class SearchForm(forms.Form):
    product = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Моля въведете продукт за търсене..'}
        ),
        label=''
    )

class SendInfoForm(forms.Form):

    name = forms.CharField(
        max_length=300,
        required=True,
        label='Име:'
    )

    email = forms.EmailField(
        max_length=500,
        required=True,
        label='Имейл:'
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={}),
        label='Съобщение'
    )