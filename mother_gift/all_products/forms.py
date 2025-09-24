from django import forms

from mother_gift.all_products.models import AllProducts


class AddProductForm(forms.ModelForm):
    class Meta:
        model = AllProducts
        fields = ('product_image', 'product_description', 'product_type', 'product_price', 'is_available')