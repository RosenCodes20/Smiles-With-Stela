from django import template


from mother_gift.common.forms import SubscribeForNewsForm

register = template.Library()

@register.simple_tag(takes_context=True)
def get_subscribe_form(context):
    request = context['request']
    return SubscribeForNewsForm(request.POST or None)