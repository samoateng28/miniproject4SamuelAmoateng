
from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Splits a string by the given argument.
    Usage: {{ value|split:"separator" }}
    """
    return value.split(arg)