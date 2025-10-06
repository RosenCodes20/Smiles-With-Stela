from django import template

from mother_gift.all_products.models import AllProducts

register = template.Library()

@register.filter
def get_cart_length():
    return AllProducts.objects.all().count()