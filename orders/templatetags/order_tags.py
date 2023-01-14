from django import template

register = template.Library()

@register.inclusion_tag('include/label.html')
def create_label(field):
    return {'field': field}