from django import forms

from mother_gift.all_products.models import AllProducts, StarRating


class AddProductForm(forms.ModelForm):
    class Meta:
        model = AllProducts
        fields = ('product_image', 'second_product_image', 'first_long_description', 'second_long_description', 'applicable_for', 'product_description', 'product_type', 'product_price', 'is_available')

class StarReviewForm(forms.ModelForm):
    class Meta:
        model = StarRating
        fields = ("person_opinion", "rating")
        widgets = {
            "rating": forms.RadioSelect(attrs={"class": "star-rating"})
        }