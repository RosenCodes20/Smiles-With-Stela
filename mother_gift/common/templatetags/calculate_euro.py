from django import template

register = template.Library()

@register.filter
def to_eur(value):
    try:
        return f'{float(value) / 1.95583:.2f}'
    except (ValueError, TypeError):
        return ""