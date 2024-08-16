# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    # Ensure field has the as_widget method before adding the class
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={"class": css_class})
    return field
