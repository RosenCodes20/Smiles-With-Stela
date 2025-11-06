from django import forms

from mother_gift.all_products.models import AllProducts


class AddProductForm(forms.ModelForm):
    class Meta:
        model = AllProducts
        fields = ('product_image', 'second_product_image', 'first_long_description', 'second_long_description', 'applicable_for', 'product_description', 'product_type', 'product_price', 'is_available')

class StarReviewForm(forms.Form):
    opinion_for_product = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "placeholder": "Въведи мнение за продука......."
        })
    )

    rating = forms.ChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={"class": "star-rating"})
    )
