from django import template


from mother_gift.common.forms import SearchForm

register = template.Library()

@register.simple_tag(takes_context=True)
def get_search_form(context):
    request = context['request']
    return SearchForm(request.GET)