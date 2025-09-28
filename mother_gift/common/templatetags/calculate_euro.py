from django import template

register = template.Library()

@register.filter
def to_eur(value):
    try:
        return round(float(value) / 1.95583, 2)
    except (ValueError, TypeError):
        return ""