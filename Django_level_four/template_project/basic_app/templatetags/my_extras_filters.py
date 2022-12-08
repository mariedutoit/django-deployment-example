# Creating extra filters to use in template tags
from django import template

register = template.Library()

# décorateur
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string
    """
    return value.replace(arg, '')
