from django import template

from mother_gift.cart.models import Cart

register = template.Library()

@register.simple_tag(takes_context=True)
def get_cart_length(context):
    request = context['request']

    if request.user.is_authenticated:
        return Cart.objects.filter(user_cart=request.user).count()

    else:
        return 0