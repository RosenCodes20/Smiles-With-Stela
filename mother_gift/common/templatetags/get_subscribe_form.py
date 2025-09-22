from django import template


from mother_gift.common.forms import SubscribeForNewsForm

register = template.Library()

@register.simple_tag(takes_context=False)
def get_subscribe_form():
    return SubscribeForNewsForm()