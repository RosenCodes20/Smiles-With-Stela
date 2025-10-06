from django import template

from mother_gift.cart.models import Cart

register = template.Library()

@register.simple_tag()
def get_cart_length():
    return Cart.objects.all().count()